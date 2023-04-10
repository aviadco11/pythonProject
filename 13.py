# age return as string, so we cast with int
num = 24
print(len(str(num)))
age = int(input("enter you age: "))
if age > 18:
    print("you are legal")
else:
    print("you are still a child")

