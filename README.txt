PYTHON BANKING SYSTEM - PROJECT PLAN
======================================

1. PROJECT TYPE
---------------
Beginner-level Python console/command-line mini project.

2. PURPOSE
----------
The project simulates basic banking operations:
- Create an account
- Login with account number and PIN
- Check balance
- Deposit money
- Withdraw money
- Transfer money
- View transaction history
- Change PIN
- Logout

3. PYTHON CONCEPTS USED
-----------------------
- Variables and data types
- if / elif / else
- while loops
- for loops
- Functions
- Lists and dictionaries
- String operations
- Exception handling
- Modules
- random
- datetime

4. FILES
--------
banking_system.py
    Main Python program.

5. IMPORTANT NOTE
-----------------
This educational version keeps accounts in memory while the program is running.
If the program is closed, the account data is cleared.

A later version can add JSON/file/database storage if your teacher asks for
permanent data storage.

6. HOW TO RUN
-------------
Install Python 3.

Open Command Prompt / Terminal in this folder and run:

    python banking_system.py

If "python" does not work on Windows, try:

    py banking_system.py

7. DEMO / TEST PLAN
-------------------
Test 1: Create Account
- Create two different accounts.
- Record both account numbers.

Test 2: Login
- Login with correct account number + PIN.
- Try a wrong PIN and confirm that login is rejected.

Test 3: Deposit
- Deposit 5000.
- Check that balance becomes 5000.

Test 4: Withdraw
- Withdraw 1000.
- Check that balance becomes 4000.
- Try withdrawing more than the balance.

Test 5: Transfer
- From account 1, transfer 1000 to account 2.
- Check that sender decreases and receiver increases.

Test 6: Transaction History
- View history and verify deposit, withdrawal and transfer entries.

Test 7: Change PIN
- Change the PIN.
- Logout and login using the new PIN.

Test 8: Logout
- Logout and confirm that the program returns to the main menu.

8. PROJECT FLOW
---------------
START
  |
CREATE ACCOUNT
  |
ACCOUNT NUMBER + PIN
  |
LOGIN
  |
ACCOUNT MENU
  |--- Check Balance
  |--- Deposit
  |--- Withdraw
  |--- Transfer
  |--- Transaction History
  |--- Change PIN
  |--- Logout
  |
MAIN MENU
  |
EXIT

9. REPORT SECTIONS TO PREPARE
-----------------------------
1. Title Page
2. Certificate / Declaration (if required)
3. Acknowledgement
4. Project Overview
5. Problem Statement
6. Project Objective
7. Main Features
8. Python Concepts Used
9. Modules Used
10. Project Structure / Flowchart
11. System Requirements
12. Algorithm / Working
13. Source Code
14. Testing and Results
15. Screenshots
16. Limitations
17. Future Scope
18. Conclusion
19. References

10. VIVA TOPICS
---------------
Be ready to explain:
- Why Python was used
- What a dictionary is
- Why functions are used
- Why random is used
- Why datetime is used
- How login works
- How deposit changes balance
- How withdrawal checks balance
- How transfer works
- How transaction history is stored
- What happens on logout
