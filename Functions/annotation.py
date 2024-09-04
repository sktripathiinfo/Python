def add(x,y):
    total = x + y
    print(total)

add(10,20)
# add("10",20)


def add(x:int,y:int)  -> int:  # here defining type of x and y

    total = x + y
    print(total)


add("10","20")


def greet(name:str, age:int, percentage:float)  -> None:
    print(name)
    print(age)
    print(percentage)

greet()

