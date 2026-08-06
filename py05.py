'''
#Prime no
n=int(input("Enter no: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(n,"is prime")
else:
    print(n,"is not prime")

#armstrong no
n=int(input("Enter no: "))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")

#fibonacci series
n=int(input("Enter no: "))
a, b = 0, 1
print(a, b, end=" ")
for _ in range(2, n):
    a, b = b, a + b
    print(b, end=" ")

#prime no less than 10000
n=10000
print("Prime numbers less than", n, "are:")
for n in range(2, n):
    c=0
    for i in range(1, n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(n, end=" ")
'''
'''
def sqr(n):
    return n*n
n=int(input("Enter no: "))
print(f"The square of {n} is {sqr(n)}")
'''
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    if n2==0:
        return "Division by zero is not allowed"
    return n1/n2



while(True):
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    ch=int(input("Enter choice (1-Add, 2-Sub, 3-Mul, 4-Div, 5-Exit): "))
    if ch==1:
        print(f"The sum of {a} and {b} is {add(a,b)}")
        continue
    elif ch==2:
        print(f"The difference of {a} and {b} is {sub(a,b)}")
        continue
    elif ch==3:
        print(f"The product of {a} and {b} is {mul(a,b)}")
        continue
    elif ch==4:
        print(f"The quotient of {a} and {b} is {div(a,b)}")
        continue
    elif ch==5:
        print("Exiting...")
        break
    elif ch.is_integer() and int(ch) not in [1, 2, 3, 4, 5]:
        print("Invalid choice")
        continue