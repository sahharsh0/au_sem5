import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [12000, 15000, 14000, 18000, 21000, 19500,
              22000, 24000, 20500, 23000, 26000, 30000]
})
print("Task 1: Monthly Sales DataFrame")
print(df)
print()

df.plot(x="Month", y="Sales", kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (in Rs.)")
plt.show()

df.plot(x="Month", y="Sales", kind="bar")
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales (in Rs.)")
plt.show()
print("Task 2: Basic plots displayed")
print()

df.plot(x="Month", y="Sales", kind="line", marker="o", color="green",
        linewidth=2, figsize=(8, 4), legend=False)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (in Rs.)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

df.plot(x="Month", y="Sales", kind="bar", color="orange",
        edgecolor="black", figsize=(8, 4), legend=False)
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales (in Rs.)")
plt.xticks(rotation=0)
plt.show()
print("Task 3: Customized plots displayed")
print()

df.plot(x="Month", y="Sales", kind="line", marker="o", color="green",
        linewidth=2, figsize=(8, 4), legend=False)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (in Rs.)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("monthly_sales.png", dpi=300, bbox_inches="tight")
print("Task 4: Plot saved as monthly_sales.png")
print("File exists:", os.path.exists("monthly_sales.png"))