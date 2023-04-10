my_file = open("my_file.txt")
for line in my_file.readlines():
    print(line, end='')

def get_name():
    name = input("enter you name : ")
    yy_file = open("names.txt", "a")
    yy_file.writelines(f"{name}\n")
    yy_file.close()

get_name()

def read_file(file):
    my_file = open(file, "r")
    for line in my_file.readlines():
        print(f"Hello {line}", end='')

read_file("names.txt")

# with example
with open("names.txt") as my_file:
    for line in my_file.readlines():
        print(line)