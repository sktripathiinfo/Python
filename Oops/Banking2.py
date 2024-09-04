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

def check_account_exists(acc_no:int) ->bool:
    global  banks
    for obj in banks:
        if obj.account == acc_no:
            return obj

    return None




while True:
    print("1. Create account")
    print("2. Show all details")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Transfer amount")
    print("6.Exit")
    choice= int(input("Enter Choice= "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)
    elif choice == 2:
        if len(banks) ==0:
            print("No accounts have been created yet")

        else:
            for account in banks:
                account.show_info()

    elif choice ==3:
        if len(banks) ==0:
            print("No account found")
        else:
            acc_no = int(input("Enter the account number to deposit = "))
            for obj in banks:
                if obj.account ==acc_no:
                    obj.deposit()
                    break

    elif choice == 4:
        if len(banks) ==0:
            print("No account found")
        else:
            acc_no = int(input("Enter the account number to withdraw = "))
            for obj in banks:
                if obj.account ==acc_no:
                    obj.withdraw()
                    break
    elif choice == 5:
        from_acc_no = int(input("Enter account no from which you want to transfer = "))
        to_acc_no   =   int(input("Enter account number from which you want to transfer = "))
        # if check_account_exists(from_acc_no) and check_account_exists(to_acc_no)
        from_acc_obj = check_account_exists(from_acc_no)
        to_acc_obj = check_account_exists(to_acc_no)
        if from_acc_obj!=None and to_acc_obj!=None:
            transfer_amount = int(input("Enter transfer amount = "))
            if from_acc_obj.balance <transfer_amount:
                print("Insuffcient balance")
            else:
                from_acc_obj.balance-=transfer_amount
                to_acc_obj.balance +=transfer_amount


        else:
            print("Account does not exists")
    elif choice == 6:
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

