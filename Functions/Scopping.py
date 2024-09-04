def addition():
    num1 = int(input("enter number 1 = "))
    num2 = int(input("enter number 1 = "))
    print(f"answer = {num1+num2}")

def substraction():
    num1 = int(input("enter number 1 = "))
    num2 = int(input("enter number 1 = "))
    print(f"answer = {num1-num2}")
# num1 num2 belongs to this function addition only
# which means they will be valid within the addition() function

addition()
substraction()

# now calling the num1 out of addition function
print(num1)