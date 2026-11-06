'''
design a class product with fields product code, name, price, quantity in stock
store inventory in a dictionary keyed by product code
provide menu to add a new product, sell a product, view full inventory, view day's sales and history
record each sale in list as transaction, generating a unique transaction id with random module
can introduce extra methods in product class for assignment
handle exceptions for selling unknown product and for selling more quantity than available in stock
'''
import random
class Product:
    def __init__(self, code, name, price, qty):
        self.code = code
        self.name = name
        self.price = price
        self.qty = qty

inventory = {}
sales = []

def add_product():
    code = input("Code: ")
    name = input("Name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    inventory[code] = Product(code, name, price, qty)

def sell_product():
    code = input("Code: ")
    qty = int(input("Quantity: "))

    if code not in inventory:
        raise Exception("Product not found")

    p = inventory[code]

    if qty > p.qty:
        raise Exception("Insufficient stock")

    p.qty -= qty
    sales.append([random.randint(1000, 9999), code, qty, qty * p.price])
    print("Sale successful")

while True:
    print("\n1.Add  2.Sell  3.Inventory  4.Sales  5.History  6.Exit")

    try:
        ch = int(input("Choice: "))

        if ch == 1:
            add_product()

        elif ch == 2:
            sell_product()

        elif ch == 3:
            for p in inventory.values():
                print(p.code, p.name, p.price, p.qty)

        elif ch == 4 or ch == 5:
            for s in sales:
                print(s)

        elif ch == 6:
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)