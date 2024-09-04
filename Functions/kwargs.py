# def add(*args , **kwargs):   #*arguments . **keyward arguments
#
#     print(**kwargs)
#     for k,v in kwargs.items():
#         print(k,v)
#     pass
#
#
# # returns dictionary
# add(name= "shubham", age=100, gender='male')


def addition(n1, n2, n3 , *args, **kwargs):
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args}")
    print(f"{kwargs}")

addition(5,10,15)
addition(5,10,15,100,200,300, )
addition(5,10,15,100,200,300, name="shubham", age="27",gender="male" )