# print abs number

number = -100

def abs(num):
    if num < 0:
        num = num * -1
    return num
        
number = abs(num=number)

print(number)