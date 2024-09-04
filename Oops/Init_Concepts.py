class Student:
    def __init__(self):
        self.name = input("Enter the name = ")
        self.age = int(input("Enter the age = "))
        self.gender = input("Enter the gender = ")
        self.roll_no = int(input("Enter the roll_no = "))
    #Method
    def info(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender ={self.gender}")




s1 = Student()

s1.info()

s2 = Student()

s2.info()









