import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Neha"],
    "Salary": [30000, 45000, 38000, 52000, 41000, 35000],
    "YearsOfService": [1, 5, 2, 7, 3, 4]
})
print("Task 1: Employee DataFrame")
print(df)
print()

def categorize(years):
    if years < 3:
        return "Junior"
    else:
        return "Senior"

print("Task 2: Testing categorize function")
print("1 year ->", categorize(1))
print("3 years ->", categorize(3))
print("6 years ->", categorize(6))
print()

df["ExperienceLevel"] = df["YearsOfService"].apply(categorize)
print("Task 3: ExperienceLevel column")
print(df)
print()

df["Bonus"] = df.apply(
    lambda row: row["Salary"] * 0.10 if row["ExperienceLevel"] == "Junior"
    else row["Salary"] * 0.15, axis=1)
print("Task 4: Bonus column")
print(df)