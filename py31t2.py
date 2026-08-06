#wapc to determine whether a student is eligible for scholarship, a student qualifies only if all tthe following conditions are satisifed
#attendance is atleast 85%
#cgpa is 8. or above, family income is less than 5 lakhs per annum, if eligible cgpa>9.5 100% scholarship, 
# if cgpa>9. 75% scholarship, if cgpa>8.5 50% scholarship, otherwise 25% scholarship, display exact reasons why student is not eligible for scholarship
at=float(input("Enter attendance percentage: "))
cg=float(input("Enter CGPA: "))
fi=float(input("Enter family income in lakhs: "))  
if at>=85:
    if cg>=8:
        if fi<5:
            if cg>9.5:
                print("Eligible for 100% scholarship")
            elif cg>9:
                print("Eligible for 75% scholarship")
            elif cg>8.5:
                print("Eligible for 50% scholarship")
            else:
                print("Eligible for 25% scholarship")
        else:
            print("Not eligible for scholarship: Family income is not less than 5 lakhs per annum")
    else:
        print("Not eligible for scholarship: CGPA is less than 8")
else:
    print("Not eligible for scholarship: Attendance is less than 85%")