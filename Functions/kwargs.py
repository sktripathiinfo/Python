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
    # print(f"{kwargs["name"]=}")


addition(5,10,15)
addition(5,10,15,100,200,300, )
addition(5,10,15,100,200,300, name="shubham", age="27",gender="male" )


# Use Case: Use **kwargs when you want to pass a variable number of keyword arguments
# to a function, especially when dealing with functions that require flexible options.

# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function to accept
# any combination of positional and keyword arguments.