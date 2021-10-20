# input setting
import sys
from itertools import combinations
import copy
import pprint


n, m = map(int,sys.stdin.readline().rstrip().split())
array = []

for i in range(n):
    array.append(list(map(int,sys.stdin.readline().rstrip().split())))

# 벽을 세울 수 있는 조합 찾기
temp = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            temp.append((i,j))

comb = list(combinations(temp, 3))

# 바이러스가 있는 곳 찾기
virus = []
def find_virus():
    for i in range(n):
        for j in range(m):
            if array[i][j] == 2:
                virus.append((i,j))

# 안전 지역 개수 세기
safe = []
def count_safe(room):
    count = 0
    for i in range(n):
        for j in range(m):
            if room[i][j] == 0:
                count += 1
    return count

height = range(0, n)
width = range(0, m)

def dfs(room, i, j):
    if i in height and j in width and room[i][j] == 0:
        room[i][j] = 2
        dfs(room, i, j+1)    
        dfs(room, i, j-1) 
        dfs(room, i+1, j) 
        dfs(room, i-1, j) 

    
find_virus()

maximum = -1 
for co1, co2, co3 in comb:
    array_temp = copy.deepcopy(array)
    array_temp[co1[0]][co1[1]] = 1
    array_temp[co2[0]][co2[1]] = 1
    array_temp[co3[0]][co3[1]] = 1
    
    for co in virus:
        array_temp[co[0]][co[1]] = 0
        dfs(array_temp, co[0], co[1])
    count = count_safe(array_temp)
    
    # pprint.pprint(array_temp, width = 20)
    # print(co1, co2, co3,count)
    
    if maximum < count:
        maximum = count
        # print(array_temp)


print(maximum)
