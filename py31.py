#odd even
'''
n=int(input('Enter a number: '))
if n%2==0:
    print('Even')
else:
    print('Odd')
'''
#leap year
'''
year=int(input('Enter a year: '))
if (year%4==0):
    if (year%100==0):
        if (year%400==0):
            print(year,'is a leap year')
        else:
            print(year,'is not a leap year')
    else:
        print(year,'is a leap year')
'''

#uppercase input lowercase output
'''
s=input('Enter a word/string: ')
if s.isupper():
    print(s.lower())
else:
    print(s,'is not in uppercase')

#chECK whether input is a letter digit or special character
'''
ch=input('Enter your input: ')
if ch.isalpha():
    print(ch,'is a letter')
elif ch.isdigit():
    print(ch,'is a digit')
elif (ch==' '):
    print(ch,'is a space')
else:
    print(ch,'is a special character')
