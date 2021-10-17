# input setting
import sys
input = sys.stdin.readline
number = input().split(0)

# number ='02984'.strip('0').split('0')

result = 0
for i in range(len(number)):
    multi = 1
    for j in number[i]:
        multi *= int(j)
    result += multi

print(result)


