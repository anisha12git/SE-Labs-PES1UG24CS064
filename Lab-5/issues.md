\# Lab 5: Static Code Analysis — Issue Report



\## Issues Identified and Fixed



| Issue | Type | Original line(s) | Description | Fix Approach |

|---|---|---:|---|---|

| Unsafe subprocess execution | Security — High | 38 | Used `subprocess.call()` with `shell=True`, creating a command-injection risk. | Replaced subprocess execution with hostname resolution using Python's `socket` module. |

| Hardcoded administrator password | Security | 8 | The administrator password was embedded in the source code. | Read the password from the `HELPDESK\_ADMIN\_PASSWORD` environment variable. |

| Mutable default argument | Bug / Maintainability | 10 | `audit\_trail=\[]` could share a list across function calls. | Changed the default to `None`. |

| Bare exception | Error handling | 23 | A bare `except:` silently swallowed errors. | Handle missing ticket IDs explicitly. |

| Invalid urgency values | Input validation | 39 | The original program accepted priorities outside the intended 1–5 range. | Validate integer input and reject values outside the permitted range. |

| Unsafe file handling | Resource management | 41 | The file was opened and closed manually without explicit encoding. | Use a context manager and UTF-8 encoding for JSON output. |

| Inconsistent function naming | Code quality | 30 | `unresolvedHighPriority()` did not follow snake\_case naming. | Renamed it to `unresolved\_high\_priority()`. |

| Missing docstrings and formatting violations | Style / Maintainability | Multiple | Functions lacked documentation and the code contained style violations. | Added docstrings and corrected formatting. |

| Unused variable | Code quality | 47 | The original `t2` variable was assigned but never used. | Removed the unused assignment. |



\## Verification Results



\- Original Pylint score: 5.53/10.

\- Final Pylint score: 10.00/10.

\- Original Bandit report: one high-severity and three low-severity findings.

\- Final Bandit report: no issues identified.

\- Original Flake8 report: formatting and code-quality violations.

\- Final Flake8 report: no findings.



\*\*Note:\*\* Original line numbers refer to the unmodified source file. The revised hostname function checks DNS resolution; it does not send an actual ping packet.



