'''
Payroll Management System: Gross Salary= Basic + DA + HRA-Income Tax
  If salary is more than 50k, then 10% tax will be deducted
  If salary is between 80k and 100k, then 30% tax will be deducted
 If salary is below 50k, then no tax will be deducted.
using if else statements and functions and loops
'''
def calculate_gross_salary(basic, da, hra):
    gross_salary = basic + da + hra
    return gross_salary
def calculate_income_tax(gross_salary):
    if gross_salary > 100000:
        tax = gross_salary * 0.30
    elif 50000 < gross_salary <= 100000:
        tax = gross_salary * 0.10
    else:
        tax = 0
    return tax
def main():
    while True:
        print("\nPayroll Management System")
        print("1. Calculate Gross Salary and Income Tax")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            basic = float(input("Enter Basic Salary: "))
            da = float(input("Enter Dearness Allowance (DA): "))
            hra = float(input("Enter House Rent Allowance (HRA): "))
            gross_salary = calculate_gross_salary(basic, da, hra)
            income_tax = calculate_income_tax(gross_salary)
            net_salary = gross_salary - income_tax
            print(f"Gross Salary: ₹{gross_salary:.2f}")
            print(f"Income Tax Deducted: ₹{income_tax:.2f}")
            print(f"Net Salary: ₹{net_salary:.2f}")
        elif choice == "2":
            print("Exiting Payroll Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()