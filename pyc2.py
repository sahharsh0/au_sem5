#wapc to calculate elec bill based on following conditions, first 100 units rs 5/unit, next 200 units rs 8/unit, above 300 units rs 10/unit, 
#if bill is above 3000 apply 10% discount, if customer is senior citizen apply additional 5% discount, display total bill before disc and final bill
#wapc to determine whether a student is eligible for scholarship, a student qualifies only if all tthe following conditions are satisifed
#attendance is atleast 85%
#cgpa is 8. or above, family income is less than 5 lakhs per annum, if eligible cgpa>9.5 100% scholarship, 
# if cgpa>9. 75% scholarship, if cgpa>8.5 50% scholarship, otherwise 25% scholarship, display exact reasons why student is not eligible for scholarship
class Student:
    def __init__(self, name, attendance, cgpa, family_income):
        self.name = name
        self.attendance = attendance
        self.cgpa = cgpa
        self.family_income = family_income


    def is_eligible_for_scholarship(self):
        if self.attendance >= 85 and self.cgpa >= 8 and self.family_income < 500000:
            return True
        else:
            return False

    def get_scholarship_details(self):
        if self.is_eligible_for_scholarship():
            if self.cgpa > 9.5:
                return "100% scholarship"
            elif self.cgpa > 9.0:
                return "75% scholarship"
            elif self.cgpa > 8.5:
                return "50% scholarship"
            else:
                return "25% scholarship"
        else:
            reasons = []
            if self.attendance < 85:
                reasons.append("Attendance is less than 85%")
            if self.cgpa < 8:
                reasons.append("CGPA is less than 8")
            if self.family_income >= 500000:
                reasons.append("Family income is not less than 5 lakhs per annum")
            return f"Not eligible for scholarship. Reasons: {', '.join(reasons)}"

class bill:
    def __init__(self, units_consumed, age):
        self.units_consumed = units_consumed
        self.age = age

    def calculate_bill(self):
        if self.units_consumed <= 100:
            bill_amount = self.units_consumed * 5
        elif self.units_consumed <= 300:
            bill_amount = 100 * 5 + (self.units_consumed - 100) * 8
        else:
            bill_amount = 100 * 5 + 200 * 8 + (self.units_consumed - 300) * 10

        total_bill_before_discount = bill_amount

        if bill_amount > 3000:
            bill_amount *= 0.9

        if self.age >= 60:
            bill_amount *= 0.95

        return total_bill_before_discount, bill_amount
print("Electricity Bill Calculation")
units = int(input("Enter units consumed: "))
age = int(input("Enter age of the customer: "))
electricity_bill = bill(units, age)
total_bill, final_bill = electricity_bill.calculate_bill()
print(f"Total bill before discount: Rs {total_bill:.2f}")
print(f"Final bill after discount: Rs {final_bill:.2f}")
print("\nScholarship Eligibility Check")
name = input("Enter student's name: ")
attendance = float(input("Enter attendance percentage: "))
cgpa = float(input("Enter CGPA: "))
family_income = float(input("Enter family income (in lakhs): ")) * 100000
student = Student(name, attendance, cgpa, family_income)
print(student.get_scholarship_details())