# Operator
# Arithmetic operators
#
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators
# ators

## Arithmetic operators
#create two variables
a=100
b=200

# addition (+) operator
print(a+b)

# subtraction (-) operator
print(a-b)

# multiplication (*) operator
print(a*b)

# division (/) operator
print(b/a)

# modulus (%) operator
print(a%b) # prints the remainder of a/b

# exponent (**) operator
print(a**b) #prints a^b
a = 10
b = 20

a+b
a-b
b - a
a*b
b/a
# Expressions
#area of a rectangle

l = 10
b = 20

area = l * b

print (area)
length = int(input("enter the length of rectangle "))
breadth = int(input("enter the breadth of rectangle "))

area = length * breadth

print("area is :" ,area)
# Area of trangle
base = int(input("enter the base of trangle "))
height = int(input("enter the height of trangle "))
area = 1/2* base * height
print("Area is: " , area)
x = float(input('enter the side x :'))
y = float(input('enter the side y :'))
h = float(input('enter the height :'))

area = 1/2(a+b)*h

print('area is : ' , area)
x = float(input('enter the side x :'))
y = float(input('enter the side y :'))
h = float(input('enter the height :'))

areaa = 1/2*(a+b) *h

print('area is : ' , area)
v = int(input('enter initial velocity :'))
u = int(input('enter final velocity :'))
a = int(input('enter the accelearation :'))

d = (v**2 - u**2) / (2*a)


print("displacement is :" , d)
# KM to miles
km = float(input('enter the km: '))
miles = km * 0.621371

print(miles)

# Area of radious
#import math class
import math

radius = float(input("enter the area of the radius"))
area = math.pi * radius**2
print("the area is :", area)
# total surface of cuboid

l = float(input("enter the length of cuboid"))
b = float(input("enter the breadth of cuboid"))
h = float(input("enter the height of cuboid"))

a = 2*(l * b + l * h + b * h )

print("total no of surface is : " , a)

# roots of quderatic  equation
import math


a = int(input("enter the value of a "))
b = int(input("enter the value of b "))
c = int(input("enter the value of c "))

root1 = (-b + math.sqrt(b**2 - 4*a*c)) /(2*a)
root2 = (-b - math.sqrt(b**2 - 4*a*c)) /(2*a)

print("the roots are ", root1,root2 )

# Python Arithmetic Operators
## Operator Description

# +=	a+=b is equivalent to a=a+b
# *=	a*=b is equivalent to a=a*b
# /=	a/=b is equivalent to a=a/b
# %=	a%=b is equivalent to a=a%b
# **=	a**=b is equivalent to a=a**b (exponent operator)
# //=	a//=b is equivalent to a=a//b (floor division)ision)
# take two variable, assign values with assignment operators
a=3
b=4

print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a+b
a+=b

print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a*b
a*=b
print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a/b
a/=b
print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a%b
a%=b
print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a**b ( exponent operator)
a**=b
print("a: "+str(a))
print("b: "+str(b))

# it is equivalent to a=a//b ( floor division)
a//=b
print("a: "+str(a))
print("b: "+str(b))
# Python Comparison Operators
# create two variables
a=100
b=200

# (==) operator, checks if two operands are equal or not
print(a==b)

# (!=) operator, checks if two operands are not equal
print(a!=b)

# (>) operator, checks left operand is greater than right operand or not
print(a>b)

# (<) operator, checks left operand is less than right operand or not
print(a<b)
#(>=) operator, checks left operand is greater than or equal to right operand or not
print(a>=b)

# (<=) operator, checks left operand is less than or equal to right operand or not
print(a<=b)
# Python Bitwise Operators
#create two variables
a=10 # binary 1010
b=7  # binary 0111

# Binary AND (&) operator, done binary AND operation
print(a&b)

# Binary OR (|) operator, done binary OR operation
print(a|b)

# Binary XOR (^) operator, done binary XOR operation
print(a^b)

# Binary ONEs Compliment (~) operator, done binary One's Compliment operation
print(~a)

# Binary Left Shift (<<) operator, done binary Left Shift operation
print(a<<1)
# Binary Right Shift (>>) operator, done binary Right Shift operation
print(a>>1)
# Python Logical Operators
#take user input as int
a=int(input())

# logical AND operation

if a%4==0 and a%3==0:
    print("divided by both 4 and 3")

# logical OR operation
if a%4==0 or a%3==0:
    print("either divided by 4 or 3")

# logical NOT operation
if not(a%4==0 or a%3==0):
    print("neither divided by 4 nor 3")
# Below is a list of operators indicating the precedence level. It’s in descending order. That means the upper group has more precedence than that of the lower group.
#
# Parenthesis – ()
# Exponentiation – **
# Compliment, unary plus and minus – ~, +, -
# Multiply, Divide, modulo – *, /, %
# Addition and Subtraction – +, -
# Right and Left Shift – >>, <<
# Bitwise AND – &
# Bitwise OR and XOR – |, ^
# Comparison Operators – ==, !=, >, <!-- <, >=, <=
# Assignment  -->Operator- =
