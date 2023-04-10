age = []
big = 0
for i in range(0, 5):
    age.append(int(input("enter you age: ")))
    if age[i] > big:
        big = age[i]
print(big)


def getname():
    names = []
    while 1>0:
        name = input("enter your name: ")
        names.append(name)
        if name == 'moshe':
            break
    return names

print(getname())


