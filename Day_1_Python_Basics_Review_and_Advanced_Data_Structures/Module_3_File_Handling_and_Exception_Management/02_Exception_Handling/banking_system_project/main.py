from utils.account_operations import create_account, load_accounts, save_accounts
from utils.exception_handlers import InsufficientFundsError, AccountNotFoundError


def main():
    while True:
        print("\nBanking System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                account_id = input("Enter Account ID: ")
                balance = float(input("Enter Initial Balance: "))
                print(create_account(account_id, balance))
            elif choice == "2":
                account_id = input("Enter Account ID: ")
                amount = float(input("Enter Deposit Amount: "))
                accounts = load_accounts()
                accounts[account_id]['balance'] += amount
                save_accounts(accounts)
                print("Deposit successful!")
            elif choice == "3":
                account_id = input("Enter Account ID: ")
                amount = float(input("Enter Withdrawal Amount: "))
                accounts = load_accounts()
                if accounts[account_id]['balance'] < amount:
                    raise InsufficientFundsError()
                accounts[account_id]['balance'] -= amount
                save_accounts(accounts)
                print("Withdrawal successful!")
            elif choice == "4":
                account_id = input("Enter Account ID: ")
                accounts = load_accounts()
                print(f"Balance: {accounts[account_id]['balance']}")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except (ValueError, InsufficientFundsError, AccountNotFoundError) as e:
            print(f"Error: {e}")
        except KeyError:
            print("Account not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
