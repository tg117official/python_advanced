import json
from config.settings import ACCOUNT_DATA_FILE

def load_accounts():
    try:
        with open(ACCOUNT_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        raise Exception("Corrupted data file.") from e

def save_accounts(accounts):
    try:
        with open(ACCOUNT_DATA_FILE, 'w') as file:
            json.dump(accounts, file)
    except IOError as e:
        raise Exception("Failed to save account data.") from e

def create_account(account_id, initial_balance):
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative.")
    accounts = load_accounts()
    if account_id in accounts:
        raise ValueError("Account already exists.")
    accounts[account_id] = {'balance': initial_balance}
    save_accounts(accounts)
    return "Account created successfully."
