a = ["daniel", "shai", "roei"]
if a[0] == "shmulik" or a[1] == "shmulik" or a[2] == "shmulik":
    print("found shmulik !!")
else:
    print("not found shmulik !!")

if "shmulik" in a:
    print("found shmulik")

first_array = []
second_array = [1, 2, 3]
third_array = [[1, 2, 3], [4,5,6], [7,8,9]]
if not first_array:
    print("first has no items")
if second_array:
    print("second array has items")
if len(second_array) > 2:
    print("we have at least 3 items in second")
print(len(third_array))

d = 5
g = 5
f = [1, 2, 3]
h = [1, 2, 3]
# check address memory is the same
if d is g:
    print("d is g")
# list is synamic, get diffrent memory address
if f is h:
    print("f is h")
if type(d) is int:
    print("d is int")