class BankAccount:
    """Class to represent a bank account with hidden attributes and methods."""

    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  # Hidden attribute
        self.__balance = initial_balance  # Hidden attribute

    # Public method to check balance
    def check_balance(self):
        return f"Account {self.__account_number}: Balance is ${self.__balance:.2f}"

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Hidden method to handle withdrawals
    def __withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    # Public method to safely access the hidden withdraw method
    def perform_withdrawal(self, amount):
        if amount > 0:
            self.__withdraw(amount)
        else:
            print("Invalid withdrawal amount.")


# Usage
print("=== Bank Account Operations ===")
# Create a bank account
account = BankAccount("1234567890", 500.00)

# Check balance
print("\nChecking Balance:")
print(account.check_balance())

# Deposit money
print("\nDepositing Money:")
account.deposit(200)  # Deposit $200
print(account.check_balance())

# Try to withdraw money
print("\nWithdrawing Money:")
account.perform_withdrawal(100)  # Withdraw $100
print(account.check_balance())

# Try to withdraw more than balance
print("\nAttempting Overdraw:")
account.perform_withdrawal(700)  # Attempt to withdraw $700
print(account.check_balance())

# Accessing hidden members (not recommended)
print("\nAccessing Hidden Members:")
# print(account.__balance)  # Error: Cannot access directly
print(account._BankAccount__balance)  # Access using name mangling (not recommended)
