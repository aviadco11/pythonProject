# exception

result = 0
try:
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    result = a / b
except ZeroDivisionError:
    print("could not divide by zero")
except FileNotFoundError:
    print("File not find")
except BaseException as e:
    print("something went wrong")
    print(e.args)
print(result)
print("sadasd")