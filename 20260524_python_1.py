accounts = {}

def create_accont(account_number, owner, initial_deposit):
    """Crate a new account in our global directory"""
    if initial_deposit < 0:
        print("initial deposit cannot be negative")
        return False
    accounts[account_number] = {
        "owner" : owner,
        "balance": initial_deposit
    }
    print(f"Account {account_number} created for {owner} with {initial_deposit}")
    return True

def deposit(account_number, amount):
    """Add money to an account"""
    if account_number not in accounts:
        print("Account is not found")
        return False
    if amount < 0:
        print("Deposit amount must be positive")
        return False
    accounts[account_number]["balance"] += amount
    print(f"Deposited ${amount}. New balance: ${accounts[account_number]['balance']}")
    return True