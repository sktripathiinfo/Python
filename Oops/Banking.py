from random import randint

class Bank:
    def __init__(self) ->None:
        self.account = randint (100000, 999999)
        self.full_name = input("Enter the name = ")
        self.phone_number = int(input("Enter the phone number = "))
        self.balance = 0

    def show_info(self):
        print(f"Account number = {self.account}")
        print(f"Full name = {self.full_name}")
        print(f"Balance = {self.balance}\n")

    def show_balance(self):
        print(f"Current_balance = {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enter amount to withdraw = "))
        if amount >self.balance:
            print("insufficient balance")

        else:
            self.balance -= amount


    def deposit(self):

        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount

banks = []
while True:
    print("1. Create account")
    print("2. Show all details")
    print("3.Exit")
    choice= int(input("Enter Choice= "))
    if choice == 1:
        obj1 = Bank()
        banks.append(obj1)
        print(banks)
    elif choice == 2:
        if len(banks) ==0:
            print("No accounts have been created yet")

        else:
            for account in banks:
                account.show_info()
    elif choice == 3:
        break
    else:
        print("Invalid Choice")
































#Using List

# banks = []
#
# x = Bank()
# banks.append(x)
# print(banks)
#
# y = Bank()
# banks.append(y)
# print(banks)
#
# banks[0].show_balance()
# banks[1].deposit()
# banks[1].show_balance()



# b1 = Bank()
# b1.show_balance()
# b1.deposit()
# b1.withdraw()
# b1.show_balance()

