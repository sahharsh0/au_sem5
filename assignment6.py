import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=90, freq="D"),
    "Temperature": np.random.randint(15, 40, 90)
})
print("Task 1: DataFrame with Date and Temperature")
print(df.head(10))
print("Shape:", df.shape)
print()
df = df.set_index("Date")
print("Task 2: Date as Index")
print(df.head())
print("Index type:", type(df.index))
print()
monthly_avg = df.resample("MS").mean()
print("Task 3: Monthly Average Temperature")
print(monthly_avg)
print()
df.plot()
plt.title("Daily Temperature Data")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.show()