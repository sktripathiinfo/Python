# Conditionals
# find the difference b/w num

a = int(input("enter the number"))
b = int(input("enter the second number"))

if a - b >= 0:
    print(a - b)
else:
    print(b - a)
# check even odd

n = int(input("enter the num "))

if n % 2 == 0:
    print("even number")

else:
    print("odd number")

# print marks are within the range

marks = int(input("enter the marks "))
if marks >= 0 and marks <= 100:
    print("Valid marks ")


else:
    print("invalid marks")
math = int(input("enter the maths number"))
phy = int(input('enter the phy number'))
chem = int(input('enter the chem number'))

if math >= 33 and phy >= 33 and chem >= 33:
    print('qulaified')
else:
    print("not qulified")
username = input("enter the username")
if username == 'shubham' and username == 'rishabh':
    print("valid username")
else:
    print("not permitted")

# elif
sk = float(input("enter the first name age "))
rk = float(input("enter the second number age "))
ss = float(input("enter the third number age "))

if sk > rk and sk > ss:
    print("sk is eldest")
else:
    if rk > ss:
        print("sk is elder")
    else:
        print("ss is elder")

sk = float(input("enter the first name age "))
rk = float(input("enter the second number age "))
ss = float(input("enter the third number age "))

if sk > rk and sk > ss:
    print("sk is eldest")
elif rk > ss:
    print("sk is elder")
else:
    print("ss is elder")
# print days

day = int(input("Enter the day"))

if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Please enter the correct day ")

Month = int(input("Enter the day"))

if Month == 1:
    print("Jan")
elif Month == 2:
    print("Feb")
elif Month == 3:
    print("March")
elif Month == 4:
    print("April")
elif Month == 5:
    print("May")
elif Month == 6:
    print("June")
elif Month == 7:
    print("July")
elif Month == 8:
    print("Aug")
elif Month == 9:
    print("Sep")
elif Month == 10:
    print("Oct")
elif Month == 11:
    print("Nov")
elif Month == 12:
    print("Dec")
else:
    print("Please enter the correct Month ")
digit = int(input("enter the digit"))

if digit == 0:
    print("zero")
elif digit == 1:
    print("one")
elif digit == 2:
    print("two")
elif digit == 3:
    print("three")
elif digit == 4:
    print("four")
elif digit == 5:
    print("five")
elif digit == 6:
    print("Six")
elif digit == 7:
    print("seven")
elif digit == 8:
    print("Eight")
elif digit == 9:
    print("nine")
elif digit == 10:
    print("ten")
else:
    print("only 0 to 10 digits are allowed")

