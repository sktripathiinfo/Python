# global keyward

a =15   # global a

def change():
    global a
    a = 30     #local variable
    print(a)

print(a)
change()
print(a)
'''
15
30
'''