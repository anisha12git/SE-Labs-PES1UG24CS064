
"""Manage IT helpdesk tickets, assignments, notes, and ticket storage."""

import json
import os
import re
import socket
from datetime import datetime
from pathlib import Path

# Global ticket state.
tickets = {}
ticket_counter = {"value": 100}
ADMIN_PASSWORD = os.getenv("HELPDESK_ADMIN_PASSWORD")


def raise_ticket(
    user: str,
    issue_type: str,
    urgency: str = "3",
    audit_trail: list | None = None,
) -> int:
    """Create a ticket and optionally record its creation in an audit trail."""
    try:
        priority = int(urgency)
    except (TypeError, ValueError) as error:
        raise ValueError(
            "Urgency must be an integer from 1 to 5."
        ) from error

    if not 1 <= priority <= 5:
        raise ValueError("Urgency must be between 1 and 5.")

    ticket_counter["value"] += 1
    ticket_id = ticket_counter["value"]
    tickets[ticket_id] = {
        "user": user,
        "issue": issue_type,
        "priority": priority,
        "tech": None,
        "notes": [],
    }

    if audit_trail is not None:
        audit_trail.append(
            f"{user} raised #{ticket_id} at {datetime.now().isoformat()}"
        )

    return ticket_id


def assign_ticket(ticket_id: int, technician: str) -> None:
    """Assign an existing ticket to a technician."""
    if ticket_id not in tickets:
        raise KeyError(f"Ticket {ticket_id} does not exist.")
    tickets[ticket_id]["tech"] = technician


def add_note(ticket_id: int, note: str) -> bool:
    """Add a note to a ticket, returning False if the ticket is missing."""
    if ticket_id not in tickets:
        print("Cannot add note: ticket does not exist.")
        return False

    tickets[ticket_id]["notes"].append(note)
    return True


def close_ticket(ticket_id: int, password: str) -> bool:
    """Close a ticket after administrator authentication."""
    if not ADMIN_PASSWORD:
        print("Cannot close ticket: administrator password is not configured.")
        return False

    if password != ADMIN_PASSWORD:
        print("Cannot close ticket: incorrect administrator password.")
        return False

    if ticket_id not in tickets:
        print(f"Cannot close ticket: ticket {ticket_id} does not exist.")
        return False

    del tickets[ticket_id]
    return True


def unresolved_high_priority() -> list[int]:
    """Return IDs of high-priority tickets without an assigned technician."""
    return [
        ticket_id
        for ticket_id, ticket in tickets.items()
        if ticket["priority"] >= 4 and ticket["tech"] is None
    ]


def ping_user_machine(hostname: str) -> bool:
    """Check DNS resolution for a hostname; this does not send a ping."""
    if not isinstance(hostname, str) or not re.fullmatch(
        r"[A-Za-z0-9.-]+", hostname
    ):
        raise ValueError("Invalid hostname.")

    try:
        socket.gethostbyname(hostname)
        return True
    except socket.gaierror:
        return False


def save_tickets(file: str = "tickets.json") -> None:
    """Save the current tickets as JSON using UTF-8 encoding."""
    with Path(file).open("w", encoding="utf-8") as ticket_file:
        json.dump(tickets, ticket_file, indent=2)


def main() -> None:
    """Run the helpdesk demonstration."""
    printer_ticket = raise_ticket("anil", "printer", "5")
    raise_ticket("meera", "wifi", "4")
    vpn_ticket = raise_ticket("joe", "vpn", "3")

    assign_ticket(printer_ticket, "Tech-Kiran")
    add_note(999, "Called user")

    print("Unassigned high priority:", unresolved_high_priority())

    level = (
        input("Urgency for a new laptop ticket (1-5, Enter for 3): ").strip()
        or "3"
    )

    try:
        raise_ticket("sana", "laptop", level)
    except ValueError as error:
        print(f"Ticket not created: {error}")

    if ADMIN_PASSWORD:
        close_ticket(vpn_ticket, ADMIN_PASSWORD)

    save_tickets()
    print("Open tickets:", list(tickets.keys()))


if __name__ == "__main__":
    main()
