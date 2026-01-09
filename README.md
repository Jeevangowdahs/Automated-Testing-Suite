# 🤖 Automated Testing Suite (Selenium)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Selenium](https://img.shields.io/badge/Tool-Selenium-green)
![Status](https://img.shields.io/badge/Test%20Status-All%20Passed-success)

## 📌 Project Overview
An automated testing framework designed to validate web application functionality. This script automates the **Quality Assurance (QA)** process by executing regression tests on login modules, inventory data, and error handling.

## 🛠️ Key Features
* **Automated Login:** Simulates user authentication flows.
* **Data Validation:** Verifies that the correct number of inventory items (6) are loaded from the database.
* **Negative Testing:** Validates error message handling for "Locked Out" users (Security Check).
* **Auto-Logging:** Generates a timestamped execution log (`test_execution_log.txt`) for audit trails.

## 📂 Test Execution Log
```text
[2026-01-09] TC_01 Login Success: PASSED
[2026-01-09] TC_02 Inventory Count: PASSED
[2026-01-09] TC_03 Locked User Check: PASSED

🚀 How to Run
1.Install dependencies:
  pip install selenium

2.Run the bot:
  python auto_tester.py
