def add(*args):   #*arguments
    print(args)
    # print(sum(args))
    pass

# args return in tuple

add([1,2],[10,20],45,100)


# add(1,2,3)
# add(100,20,30,50,60)
# add(12, 24)


# Use Case: Use *args when you want to pass a variable number of positional arguments to a function.
#
# **kwargs (Variable-Length Keyword Arguments)
# The **kwargs syntax allows a function to accept an arbitrary number of keyword arguments.
# **kwargs collects these into a dictionary.