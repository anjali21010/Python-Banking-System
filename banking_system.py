import random
from datetime import datetime

# All accounts are stored here while the program is running.
accounts = {}
logged_in_account = None


def generate_account_number():
    """Generate a unique 6-digit account number."""
    while True:
        account_number = str(random.randint(100000, 999999))
        if account_number not in accounts:
            return account_number


def create_account():
    print("\n" + "=" * 40)
    print("           CREATE ACCOUNT")
    print("=" * 40)

    name = input("Enter your name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    phone = input("Enter phone number: ").strip()
    while not phone.isdigit() or len(phone) != 10:
        print("Please enter a valid 10-digit phone number.")
        phone = input("Enter phone number: ").strip()

    pin = input("Create a 4-digit PIN: ").strip()
    while not pin.isdigit() or len(pin) != 4:
        print("PIN must contain exactly 4 digits.")
        pin = input("Create a 4-digit PIN: ").strip()

    account_number = generate_account_number()

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "history": []
    }

    print("\nAccount created successfully!")
    print(f"Your Account Number is: {account_number}")
    print("Please remember your Account Number and PIN.")


def login():
    global logged_in_account

    print("\n" + "=" * 40)
    print("                LOGIN")
    print("=" * 40)

    account_number = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    if account_number in accounts and accounts[account_number]["pin"] == pin:
        logged_in_account = account_number
        print(f"\nLogin successful! Welcome, {accounts[account_number]['name']}.")
        account_menu()
    else:
        print("\nInvalid Account Number or PIN.")


def add_transaction(account_number, transaction_type, amount, details=""):
    accounts[account_number]["history"].append({
        "type": transaction_type,
        "amount": amount,
        "details": details,
        "date_time": datetime.now().strftime("%d-%m-%Y %I:%M %p")
    })


def check_balance():
    account = accounts[logged_in_account]

    print("\n" + "=" * 40)
    print("            ACCOUNT BALANCE")
    print("=" * 40)
    print(f"Account Holder : {account['name']}")
    print(f"Account Number : {logged_in_account}")
    print(f"Current Balance: ₹{account['balance']:.2f}")


def deposit():
    account = accounts[logged_in_account]

    print("\n" + "=" * 40)
    print("             DEPOSIT MONEY")
    print("=" * 40)

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        account["balance"] += amount
        add_transaction(logged_in_account, "Deposit", amount)

        print(f"₹{amount:.2f} deposited successfully.")
        print(f"Current Balance: ₹{account['balance']:.2f}")

    except ValueError:
        print("Please enter a valid numeric amount.")


def withdraw():
    account = accounts[logged_in_account]

    print("\n" + "=" * 40)
    print("            WITHDRAW MONEY")
    print("=" * 40)

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > account["balance"]:
            print("Insufficient balance!")
            return

        account["balance"] -= amount
        add_transaction(logged_in_account, "Withdrawal", amount)

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Remaining Balance: ₹{account['balance']:.2f}")

    except ValueError:
        print("Please enter a valid numeric amount.")


def transfer():
    sender = accounts[logged_in_account]

    print("\n" + "=" * 40)
    print("           TRANSFER MONEY")
    print("=" * 40)

    receiver_number = input("Enter receiver account number: ").strip()

    if receiver_number not in accounts:
        print("Receiver account not found.")
        return

    if receiver_number == logged_in_account:
        print("You cannot transfer money to your own account.")
        return

    try:
        amount = float(input("Enter amount to transfer: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > sender["balance"]:
            print("Insufficient balance!")
            return

        receiver = accounts[receiver_number]

        sender["balance"] -= amount
        receiver["balance"] += amount

        add_transaction(
            logged_in_account,
            "Transfer",
            amount,
            f"To Account {receiver_number}"
        )

        add_transaction(
            receiver_number,
            "Received",
            amount,
            f"From Account {logged_in_account}"
        )

        print(f"₹{amount:.2f} transferred successfully.")
        print(f"Your Current Balance: ₹{sender['balance']:.2f}")

    except ValueError:
        print("Please enter a valid numeric amount.")


def transaction_history():
    account = accounts[logged_in_account]

    print("\n" + "=" * 55)
    print("               TRANSACTION HISTORY")
    print("=" * 55)

    if not account["history"]:
        print("No transactions found.")
        return

    for number, transaction in enumerate(account["history"], start=1):
        print(f"\nTransaction {number}")
        print(f"Type      : {transaction['type']}")
        print(f"Amount    : ₹{transaction['amount']:.2f}")
        print(f"Details   : {transaction['details']}")
        print(f"Date/Time : {transaction['date_time']}")


def change_pin():
    account = accounts[logged_in_account]

    print("\n" + "=" * 40)
    print("               CHANGE PIN")
    print("=" * 40)

    old_pin = input("Enter old PIN: ").strip()

    if old_pin != account["pin"]:
        print("Incorrect old PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ").strip()

    while not new_pin.isdigit() or len(new_pin) != 4:
        print("PIN must contain exactly 4 digits.")
        new_pin = input("Enter new 4-digit PIN: ").strip()

    confirm_pin = input("Confirm new PIN: ").strip()

    if new_pin != confirm_pin:
        print("New PIN and confirmation PIN do not match.")
        return

    account["pin"] = new_pin
    print("PIN changed successfully.")


def account_menu():
    global logged_in_account

    while logged_in_account is not None:
        print("\n" + "=" * 40)
        print("             ACCOUNT MENU")
        print("=" * 40)
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            change_pin()
        elif choice == "7":
            print("\nLogged out successfully.")
            logged_in_account = None
        else:
            print("Invalid choice. Please select 1 to 7.")


def main():
    while True:
        print("\n" + "=" * 45)
        print("          WELCOME TO PYTHON BANK")
        print("=" * 45)
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\nThank you for using Python Bank.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
