#wapc to calculate elec bill based on following conditions, first 100 units rs 5/unit, next 200 units rs 8/unit, above 300 units rs 10/unit, 
#if bill is above 3000 apply 10% discount, if customer is senior citizen apply additional 5% discount, display total bill before disc and final bill
u=int(input("Enter units consumed: "))
a=int(input("Enter age of customer: "))
if u<=100:
    bill=u*5
elif u<=300:
    bill=100*5+(u-100)*8
else:
    bill=100*5+200*8+(u-300)*10
print("Total bill before discount: ", bill)
if bill>3000:
    bill=bill*0.9
if a>=60:
    bill=bill*0.95
print("Final bill after discount: ", bill)