\# Lab 5: Static Code Analysis — Reflection



\## 1. What is static code analysis, and why is it useful?



Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, maintainability problems, and style violations early in development.



\## 2. What are the differences between Pylint, Bandit, and Flake8?



\- \*\*Pylint\*\* checks code quality, naming, documentation, and potential programming errors.

\- \*\*Bandit\*\* identifies common security risks in Python code.

\- \*\*Flake8\*\* checks formatting, whitespace, line length, and other style violations.



Using all three provides complementary checks.



\## 3. What issues did you find, and how did you fix them?



The original program contained unsafe subprocess execution with `shell=True`, a hardcoded administrator password, a mutable default argument, a bare exception, missing file-handling safeguards, invalid urgency values, inconsistent naming, missing docstrings, and formatting problems.



I removed shell-based execution, moved the administrator password to an environment variable, replaced the mutable default with `None`, handled missing tickets explicitly, validated urgency, used a context manager for JSON output, improved naming and documentation, and corrected formatting.



\## 4. How did static analysis improve the program, and what are its limitations?



The tools helped identify security risks, style violations, and maintainability problems. After the changes, Pylint reported 10.00/10, Bandit reported no issues, and Flake8 reported no findings.



However, static analysis cannot guarantee that a program is completely secure or functionally correct. It should be combined with functional testing, code review, and appropriate runtime checks.



