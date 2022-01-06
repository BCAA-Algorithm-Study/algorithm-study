# input setting
import sys
input = sys.stdin.readline

n = int(input())
a = []
b = []
for i in range(n):
    temp = int(input())
    a.append(temp)

for i in range(n):
    temp = int(input())
    b.append(temp)

cycle_array = []
moved_cow = []

for i in range(n):
    temp = []
    displaced_num = a[i]
    if displaced_num in moved_cow:
        continue
    while True:
        proper_idx = b.index(displaced_num)
        if displaced_num == a[proper_idx]: # a의 소가 올바른 위치에 있을 때 break
            break
        displaced_num = a[proper_idx]
        temp.append(displaced_num)
        if displaced_num == a[i]: # 
            cycle_array.append(temp)
            moved_cow.extend(temp)
            break

if any(cycle_array):
    print(len(cycle_array), max(len(length) for length in cycle_array))
else:
    print(0,-1)

# print(cycle_array)