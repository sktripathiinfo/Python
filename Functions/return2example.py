"""
ask 2 numbers from user
calculate total of 2 nums
print if the sum is odd or even

"""

def add (n1, n2):
    total = n1 +n2
    # print(total)
    return total
def check(num):
    if num%2 ==0:
        # print("even")
        return "even"
    else:
        # print("odd")
        return "odd"

x = int(input("enter num1 = "))
y = int(input("enter num2 = "))

s= add(x ,y )

print(check(s))


