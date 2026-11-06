import pandas as pd
import urllib.request
import os

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
urllib.request.urlretrieve(url, "titanic.csv")
print("Task 1: Dataset downloaded")
print("File size:", os.path.getsize("titanic.csv"), "bytes")
print()

pd.set_option("display.max_columns", None)
df = pd.read_csv("titanic.csv")
print("Task 2: First 10 rows")
print(df.head(10))
print()

print("Task 3: DataFrame info")
df.info(memory_usage="deep")
print()

df = pd.read_csv("titanic.csv")
before = df.memory_usage(deep=True).sum()
int_cols = df.select_dtypes(include="int64").columns
df[int_cols] = df[int_cols].astype("int32")
float_cols = df.select_dtypes(include="float64").columns
df[float_cols] = df[float_cols].astype("float32")
df["Sex"] = df["Sex"].astype("category")
df["Embarked"] = df["Embarked"].astype("category")
after = df.memory_usage(deep=True).sum()
print("Task 4: Memory Optimization")
print("Memory before:", before, "bytes")
print("Memory after:", after, "bytes")
print("Memory saved: {:.1f}%".format((before - after) / before * 100))
print(df.dtypes)
print()

df = pd.read_csv("titanic.csv")
num_cols = df.select_dtypes(include="number")
stats = num_cols.agg(["mean", "median", "std"]).T
print("Task 5: Statistical Summary (mean, median, std)")
print(stats.round(2))