# input setting
import sys
n = int(sys.stdin.readline().rstrip())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

array.sort()
sum = array[0]
for i in range(1, len(array)):
    sum += array[i]
    if i != len(array)-1:
        sum = 2*sum


print(sum)    

