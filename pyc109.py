#code to create  customer clas where customer will have following attribute
#name, id, branch name,balance, amount
#customer can perform following opt: deposit, withdraw, check statement
class Customer:
    def __init__(self, name, customer_id, branch_name, balance):
        self.name = name
        self.customer_id = customer_id
        self.branch_name = branch_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_statement(self):
        print(f"Customer ID: {self.customer_id}, Name: {self.name}, Branch: {self.branch_name}, Balance: {self.balance}")
ob = Customer("John Doe", 12345, "Main Branch", 1000)
ob.check_statement()
ob.deposit(500)
ob.withdraw(200)
ob.check_statement()
