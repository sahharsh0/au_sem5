'''
products = (     ("Laptop", 55000, 12), 
    ("Mobile", 25000, 25), 
    ("Tablet", 30000, 18), 
    ("Monitor", 15000, 10), 
    ("Keyboard", 2000, 40) 
) 
 
ducts according to price in ascending order. 
b.	Sort products according to price in descending order. 
c.	Sort products according to stock quantity. 
d.	Find the most expensive product. 
e.	Find the product with the highest stock. 
Use the key parameter of sorted() 
'''
products = (
    ("Laptop", 55000, 12),
    ("Mobile", 25000, 25),
    ("Tablet", 30000, 18),
    ("Monitor", 15000, 10),
    ("Keyboard", 2000, 40)
)
ascending = sorted(products, key=lambda x: x[1])
print("Price in ascending order:")
print(ascending)
descending = sorted(products, key=lambda x: x[1], reverse=True)
print("\nPrice in descending order:")
print(descending)
stock = sorted(products, key=lambda x: x[2])
print("\nAccording to stock quantity:")
print(stock)
expensive = max(products, key=lambda x: x[1])
print("\nMost expensive product:")
print(expensive)
highest_stock = max(products, key=lambda x: x[2])
print("\nProduct with highest stock:")
print(highest_stock)