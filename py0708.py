'''
Bank Account Management System: Simulate a basic banking system (deposit, withdraw, balance check)SS
'''
def deposit(balance, amount):
    balance += amount
    print(f"Deposited: ₹{amount}. New balance: ₹{balance}")
    return balance
def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Withdrew: ₹{amount}. New balance: ₹{balance}")
    return balance
def check_balance(balance):
    print(f"Current balance: ₹{balance}")
def main():
    balance = 0
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print("Thank you for using banking system.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    