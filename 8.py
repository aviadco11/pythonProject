## 8 - LOOPS

names = ["inbar", "lanir", "eran", "kfir", "alina"]
numbers = [1, 2, 3, 4, 5, 6, 7]
print(list(range(5)))
print(list(range(2, 5)))
print(list(range(2, 15, 3)))
print(list(range(20, 1, -3)))
for name in names:
    print(name, end=',')

for i in range(5):
    print(names[i])

for i in range(len(names)):
    print(names[i])

# here is not change because a scope, it's temporary
for name in names:
    name = "liran"

# here is change value
for i in range(len(names)):
    name = "liran"

a = 0
while a < 5:
    print(a)
    a += 1

# continue skip on value, break = get out from loop, else = if loop finish and not break
for number in numbers:
    if number == 3:
        continue
    if number == 2:
        break
    print(number)
else:
    print("finish successfully")

a = 0
while a < 5:
    print(a)
    a += 1
else:
    print("finished")