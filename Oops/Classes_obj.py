
class Student:
    def __init__(self) -> None:
        self.name = input("enter name = ")
        self.age = int(input("enter age = "))

    def display_info(self):
        print(f"name ={self.name}")
        print(f"name ={self.age}")

    def change_name(self, new_name:str):
        self.name = new_name

s1 = Student()
s1.display_info()
s1.change_name("XYZ")
s1.display_info()

