class Student:
    roll_no = 0
    name = ''
    age = 0
    gender = ''
    address = ''


    #Method
    def info(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender ={self.gender}")

    def set_info(self):

        self.name = input("Enter the name = ")
        self.age = int(input("Enter the name = "))
        self.gender= input("Enter the name = ")
        self.roll_no = int(input("Enter the roll_no = "))

s1 = Student()
s2 = Student()
s1.set_info()
s2.set_info()





s1.roll_no =10
s1.name = "shubham"
s1.age =30
s1.info()
s2.info()


