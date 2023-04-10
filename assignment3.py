from PIL import Image
# 1+2
try:
    a = 1 / 0
except:
    print("divide by zero")

#3 the code is legal
try :
    x = 1
finally :
    print("finally")

#4 BaseException, Dividebyzero, out_of_range

#5 it's not mention the type of exception to catch

#6 read from file that not exist
try:
    new_file = open('InnitialCommit.txt', 'r')
except IOError as e:
    print(e.args)

#6 ZeroDivisionError
try:
    a = 1/0
except ZeroDivisionError as e:
    print(e.args)

#7
def write_to_file(name, file):
    my_file = open(file, "w", encoding="utf-8")
    my_file.writelines(f"{name}\n")
    my_file.close()

def read_from_file(filename):
    my_file = open(filename, "r", encoding="utf-8")
    for line in my_file.readlines():
        print(f"{line}", end='')
    my_file.close()

write_to_file("אביעד","words3.txt")
read_from_file("words3.txt")


im = Image.open("download.png")
im.show()
im.close()
