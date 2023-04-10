
# A
x = 12
y = 16
if x > y:
    print("BIG")
elif y > x:
    print("small")

# B
for i in range(0, 5):
    print(i)

# C
num = 1
if num == 1:
    print("summer")
elif num == 2:
    print("winter")
elif num == 3:
    print("fall")
elif num == 4:
    print("spring")

# D
# 1. 10
# 2. 10
count = 1
while count < 11:
    print(count)
    count = count+1

# E
age = 39
fllastname = 'c'
currency = 3.66
flweabroad = True
apartmentnumber = 21
print("age: {0} ".format(age))
print("first letter lastname: {0} ".format(fllastname))
print("shekels-dollar currency: {0} ".format(currency))
print("Did you flwe abroad: {0} ".format(flweabroad))
print("apartmentnumber: {0} ".format(apartmentnumber))
print("age+currency = {0} ".format(age+currency))

# F
phone_number = input("enter you phone number1: ")
print("phone number1: {0}".format(phone_number))

# G
def printHello():
    print("hello")

def calculate():
    print(5+3.2)

printHello()
calculate()

# H
def getname(name):
    print(name)

def getnumber(num):
    print(num/2)

getname("aviad")
getnumber(3)

# I
def getnumbers(a, b):
    return (a + b)

def getstr(a, b):
    return (a + " " + b)

print(getnumbers(4,6))
print(getstr("dsf", "111"))

# K, pyramid
for i in range(0, 6):
    for j in range(0, i):
        print("#", end = "")
    print("\t")

# L-1
print("\n")
for i in range(1, 8):
    for j in range(1, 8):
        if i == j:
            print("#", end=" ")
        elif i + j == 8:
            print("#", end=" ")
        else: print(" ", end=" ")
    print("\t")

# L-2
def print_pyramid(height):
    for i in range(1, height+1):
        print(i*"#")

print_pyramid(8)

# L-3
def print_pyramid3(hight):
    for i in range(1, hight + 1):
        for j in range(1, hight + 1):
            if j< i:
                print("#", end='')
        print()

print_pyramid3(8)

# M
def get_num_from_input():
    num = input("enter you phone number: ")
    return num
