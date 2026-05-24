class Account:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposited {amount}. New balance: {self.balance}")
    
    def get_balane(self):
        return self.balance
    

alice_account = Account('Alice', 'ACC001', 1000)
bob_account = Account('Bob', 'ACC002', 500)

# print(f"Alice's account details: {alice_account.owner}, {alice_account.account_number}, {alice_account.balance}")
# print(f"Bob's account details: {bob_account.owner}, {bob_account.account_number}, {bob_account.balance}")

# alice_account.deposit(500)
# bob_account.deposit(100)



# print(f"Alice's account details: {alice_account.owner}, {alice_account.account_number}, {alice_account.balance}")
# print(f"Bob's account details: {bob_account.owner}, {bob_account.account_number}, {bob_account.balance}")

#====================

class SecuredAccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance   #Want to make to PRIVATE

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")
    
    def get_balane(self):
        return self.__balance
    
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balane: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


alice = SecuredAccount("Alice", "ACC001", 1000)
alice.__balance = 100000

print(f"Alice's account details: {alice.owner}, {alice.account_number}, {alice.__balance}")

print(f"Alice actual balance: {alice.get_balane()}")
alice.deposit(500)

print(alice)
