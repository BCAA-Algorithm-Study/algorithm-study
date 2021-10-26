# input setting
import sys
from collections import deque
import pprint

n, l, r = map(int,sys.stdin.readline().rstrip().split())
array = []

for i in range(n):
    array.append(list(map(int,sys.stdin.readline().rstrip().split())))

size = range(n)

def union(group):
    s = 0
    for i, j in group:
        s += array[i][j]
    
    for i, j in group:
        array[i][j] = s // len(group)

count = 0


def open_bfs():
    groups = []
    visited = []
    for i in range(n):
        for j in range(n):
            if [i,j] not in visited:
                q = deque([[i,j]])
                group = []
                move = [(0,1),(0,-1),(1,0),(-1,0)]
                while q:
                    current_x, current_y = q.popleft()
                    if [current_x, current_y] not in visited:
                        visited.append([current_x, current_y])
                        group.append([current_x, current_y])
                        for dx, dy in move:
                            next_x, next_y = current_x + dx, current_y + dy
                            if next_x in size and next_y in size and l <= abs(array[next_x][next_y] - array[current_x][current_y]) <= r:
                                q.append([next_x,next_y])
                # print(f'group: {group}')              
                groups.append(group)
                union(group)
    # pprint.pprint(array, width=20)
    # print(f'groups : {groups}')
    return groups

while True:
    groups = open_bfs()
    # print(f'group개수: {len(groups)}')
    if len(groups) == n*n :
        print(count)
        break
    else:
        count+=1
    
    


                


    