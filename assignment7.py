import pandas as pd

df = pd.DataFrame({
    "ProductID": [101, 102, 103, 1001, 1002, 1003],
    "ProductName": ["Laptop", "Smartphone", "Headphones", "Sofa", "Table", "Chair"],
    "Price": [55000, 30000, 2500, 25000, 7500, 3500]
})
print("Task 1: Product DataFrame")
print(df)
print()

df["DiscountedPrice"] = df["Price"].apply(lambda p: p * 0.90)
print("Task 2: DiscountedPrice (10% discount)")
print(df)
print()

df["Category"] = df["ProductID"].map(
    lambda pid: "Electronics" if pid < 1000 else "Furniture")
print("Task 3: Category based on ProductID")
print(df)
print()

df["PriceRange"] = df["Price"].apply(
    lambda p: "Low" if p < 5000 else ("Medium" if p < 30000 else "High"))
print("Task 4: PriceRange based on Price")
print(df)