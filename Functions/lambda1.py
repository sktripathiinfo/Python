# take a argument which will be number
# make a list 0 to n


make_list = lambda n:[i for i in range(0,n+1)]


length = int(input("Enter length = "))
list1 = make_list(5)
list2 = make_list(15)
print(f"{list1 = }")
print(f"{list2 = }")
