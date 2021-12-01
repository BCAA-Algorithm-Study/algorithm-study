# input setting
import sys
import pprint
input = sys.stdin.readline
n = int(input())

INF = 1e9
array = [[INF]*n for _ in range(n)]
for i in range(n):
    array[i][i] = 0
    temp = list(input())[:-1]
    for j in range(n):
        if temp[j] =='Y':
            array[i][j] = 1
# pprint.pprint(array,depth = 200)
for k in range(n):
    for i in range(n):
        for j in range(n):
            array[i][j] = min(array[i][j], array[i][k]+array[k][j])
# pprint.pprint(array,depth=200)
max = 0
for i in range(n):
    friend_2 = array[i].count(1) + array[i].count(2)
    if friend_2 > max:
        max = friend_2
print(max)

