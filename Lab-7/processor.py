
def decode_promo_voucher(voucher_code):
    if not isinstance(voucher_code, str):
        return "Invalid voucher code"

    code = voucher_code.strip()

    if code.count('-') != 1:
        return "Invalid voucher format"

    prefix, pct_str = code.split('-')

    prefix = prefix.strip()
    pct_str = pct_str.strip()

    if not prefix or not prefix.isalnum():
        return "Invalid voucher prefix"

    try:
        percentage = int(pct_str)
    except (ValueError, TypeError):
        return "Invalid voucher percentage"

    if not 0 <= percentage <= 100:
        return "Invalid voucher percentage"

    return f"Valid {prefix.upper()}: {percentage}% OFF"


def calculate_seat_tier_price(tier_spec):
    if not isinstance(tier_spec, str):
        return "Invalid tier specification"

    if tier_spec.count('@') != 1:
        return "Invalid tier format"

    tier_part, row_part = tier_spec.split('@')

    tier = tier_part.strip().upper()
    row_part = row_part.strip()

    tier_rates = {
        "VIP": 150.0,
        "PREMIUM": 90.0,
        "GENERAL": 45.0
    }

    if tier not in tier_rates:
        return "Invalid seat tier"

    try:
        row = int(row_part)
    except (ValueError, TypeError, OverflowError):
        return "Invalid row number"

    if row < 0:
        return "Invalid row number"

    try:
        return tier_rates[tier] + (row * 2.0)
    except (OverflowError, ValueError):
        return "Invalid row number"


def parse_attendee_badge(badge_csv):
    if not isinstance(badge_csv, str):
        return "Invalid attendee badge"

    tokens = badge_csv.split(',')

    if len(tokens) != 3:
        return "Invalid badge format"

    name = tokens[0].strip()
    age_str = tokens[1].strip()
    seat = tokens[2].strip()

    if not name or not seat:
        return "Invalid name or seat"

    try:
        age = int(age_str)
    except (ValueError, TypeError, OverflowError):
        return "Invalid attendee age"

    if age < 0:
        return "Invalid attendee age"

    category = "Child" if age < 18 else "Adult"

    return f"{name} [{category}] - Seat {seat}"


def main():
    print("==== Running decode_promo_voucher ====")
    v_input = input("Enter voucher (e.g. EARLY-20): ")
    print("Voucher:", decode_promo_voucher(v_input))

    print("\n==== Running calculate_seat_tier_price ====")
    t_input = input("Enter tier spec (e.g. VIP@4): ")
    print("Seat Price: $", calculate_seat_tier_price(t_input))

    print("\n==== Running parse_attendee_badge ====")
    b_input = input("Enter badge CSV (Name,Age,Seat): ")
    print("Badge:", parse_attendee_badge(b_input))


if __name__ == "__main__":
    main()
