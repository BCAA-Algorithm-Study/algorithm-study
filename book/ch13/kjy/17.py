# input setting
import sys
import heapq
from collections import deque
import pprint

n, k = map(int,sys.stdin.readline().rstrip().split())

array = []
for i in range(n):
    array.append(list(map(int,sys.stdin.readline().rstrip().split())))

s,x,y = map(int,sys.stdin.readline().rstrip().split())

x=x-1
y=y-1

def find_index(array):
    q = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] != 0:
                q.append((array[i][j], 0, i, j))
    q.sort()
    return q

# bfs
q = deque(find_index(array))
range_possible = range(n)
direction = [(0,1),(0,-1),(1,0),(-1,0)]
time = 0

while q and time + 1 < s:
    number, time, current_x, current_y = q.popleft()
    for dx, dy in direction:
        next_x, next_y = current_x + dx, current_y + dy
        if next_x in range_possible and next_y in range_possible and array[next_x][next_y] == 0:
            
            array[next_x][next_y] = number
            q.append((number, time + 1, next_x, next_y))
    # print(time)
    # pprint.pprint(array, width = 20)

print(array[x][y]) 


