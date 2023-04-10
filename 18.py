# we get error runtime divide by zero

result = 0
try:
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    result = a / b
except BaseException as e:
    print("something went wrong")
    print(e.args)
print(result)
print("sadasd")