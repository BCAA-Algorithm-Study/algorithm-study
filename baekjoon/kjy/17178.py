# input setting
import copy
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    temp = input().split()
    array.extend(temp)

sorted_array = copy.deepcopy(array)
sorted_array = sorted(sorted_array, key=lambda x: (x.split('-')[0], int(x.split('-')[1])))
stack = []

array = deque(array)
print(sorted_array)
for i in range(len(sorted_array)):
    
    if not stack:
        stack.append(array.popleft())
        print(stack, sorted_array[i], array)

    while stack and array:
        if stack[-1] == sorted_array[i]:
            stack.pop()
            break
        else:
            stack.append(array.popleft())
        print(stack, sorted_array[i], array)

if stack:
    print('BAD')
else:
    print('GOOD')