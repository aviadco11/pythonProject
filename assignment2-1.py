from assignment2 import get_num_from_input as getnum
num = getnum()
sum = 0
while int(num) > 1:
        sum += int(num) % 10
        num = int(int(num) / 10)
print(sum+num)