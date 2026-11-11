\# L6\_L7\_06 — Event Ticket Tier



\## Lab 7: Fuzz Testing with Hypothesis



\### About



This project demonstrates fuzz testing using the Hypothesis library in Python. It focuses on identifying and fixing input validation bugs in three functions related to promotional voucher codes, seat tier price calculations, and attendee badge parsing.



\### Files



| File | Description |

|---|---|

| `processor.py` | Corrected application with input validation |

| `test\_processor.py` | Hypothesis-based fuzz tests for all three functions |

| `screenshots/` | Screenshots showing original execution, failing tests, corrected application, and successful test results |



\### Testing



Install the required libraries:



`pip install hypothesis pytest`



Run the fuzz tests:



`python -m pytest test\_processor.py`



\### Test Results



All 3 Hypothesis-based tests passed successfully after fixing the identified input validation bugs.



\### Repository



All Lab 7 source code, test files, and execution screenshots are maintained in this folder.

