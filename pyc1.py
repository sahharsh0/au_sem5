#develop grade card
#91-10 O, 81-90 A+, 71-80 A, 61-70 B+, 51-60 B, 41-50 C, 34-40 D, below 34 F
c= int(input("Enter marks for c: "))
cplus = int(input("Enter marks for c++: "))
java = int(input("Enter marks for java: "))
total = c + cplus + java
avg = total / 3
if avg >= 91 and avg <= 100:
    print("Grade: O")
elif avg >= 81 and avg <= 90:
    print("Grade: A+")
elif avg >= 71 and avg <= 80:
    print("Grade: A")
elif avg >= 61 and avg <= 70:
    print("Grade: B+")
elif avg >= 51 and avg <= 60:
    print("Grade: B")
elif avg >= 41 and avg <= 50:
    print("Grade: C")
elif avg >= 34 and avg <= 40:
    print("Grade: D")
else:
    print("Grade: F")
