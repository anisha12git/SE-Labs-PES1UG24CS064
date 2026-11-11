# L6_L7_06 — Event Ticket Tier

## Lab 7: Fuzz Testing with Hypothesis

### About

This project demonstrates fuzz testing using the Hypothesis library in Python. It focuses on identifying and fixing input validation bugs in three functions related to promotional voucher codes, seat tier price calculations, and attendee badge parsing.

### Files

| File | Description |
|---|---|
| `processor.py` | Corrected application with input validation |
| `test_processor.py` | Hypothesis-based fuzz tests for all three functions |
| `screenshots/` | Screenshots of original execution, failing tests, corrected application, and successful test results |

### Requirements

- Python 3
- Hypothesis
- Pytest

### Installation

Install the required libraries using:

```bash
pip install hypothesis pytest
```

### Running the Application

```bash
python processor.py
```

### Running the Tests

Execute the Hypothesis-based fuzz tests using:

```bash
python -m pytest test_processor.py
```

### Test Results

The original application was tested using Hypothesis to identify input validation bugs.

After implementing the necessary fixes, all three Hypothesis-based tests passed successfully.

**Final Result: 3 passed**

### Project Structure

```text
Lab-7/
│
├── processor.py
├── test_processor.py
├── README.md
│
└── screenshots/
    ├── 1_original_application.png
    ├── 2a_failing_tests.png
    ├── 2b_failing_tests.png
    ├── 2c_failing_tests.png
    ├── 2d_failing_tests.png
    ├── 2e_failing_tests.png
    ├── 2f_failing_tests.png
    ├── 3_fixed_application.png
    └── 4_passing_tests.png
```

All Lab 7 source code, test files, and execution evidence are maintained in this folder.
