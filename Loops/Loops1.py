# table of any number

n = int(input("enter thwe number: "))

counter = 1

while counter <= 10:
    print(n, 'x', counter, '=', n * counter)
    counter += 1

# print hello 10 times

count = 0
while count < 10:
    # print("hello shubham")
    print(count, "hello shubham")
    count = count + 1
n = 1234
while n > 0:
    r = n % 10
    n = n // 10
    print(r)
n = int(input("enter the number: "))

while n > 0:
    r = n % 10
    n = n // 10
    print("the reverse num is", r)
# count the digit

n = int(input("enter a number "))
counter = 0
while n > 0:
    n = n // 10
    counter += 1
    # print("number of digits are", counter)
print("number of digits are", counter)
# sum of digits

n = int(input("enter the number"))
sum = 0
while n > 0:
    remainder = n % 10
    n = n // 10
    sum = sum + remainder
print("the sum is: ", sum)

# reverse a number
n = int(input("enter a number"))

rev = 0

while n > 0:
    remainder = n % 10
    n = n // 10
    rev = rev * 10 + remainder
print("the reversed number is: ", rev)
#  check palindrome
num = int(input("enter a number"))

m = num
rev = 0

while num > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
if m == rev:
    print("the number is palindrome")
else:
    print("it is not palindrome number")

# find the sum of given number
sum_of_num = int(input("enter the number"))

sum = 0
count = 0

while count < sum_of_num:
    n = int(input("enter the number: "))
    sum = sum + n
    count += 1
    print(sum)
# sum of positive and negative number
num_of_num = int(input("enter the number "))

count = 0
max = int(input("enter the number"))

while count < num_of_num - 1:
    n = int(input("enter the number: "))
    if n > max:
        max = n
        count += 1
print("max num is:", max)



