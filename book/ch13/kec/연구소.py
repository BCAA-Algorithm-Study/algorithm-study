from collections import deque
from itertools import combinations
import copy
import pprint

def build_wall(lab_map, wall) :
    temp = copy.deepcopy(lab_map)
    for i, j in wall :
        temp[i][j] = 1
    return temp



# 바이러스 확산함수
def diffusion(lab_map, virus) :
    n = len(lab_map)
    m = len(lab_map[0])
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    temp = copy.deepcopy(lab_map)
    while virus :
        x, y = virus.popleft()
        for dx, dy in move :
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m :
                if temp[nx][ny] == 0 :
                    virus.append((nx, ny))
                    temp[nx][ny] = 2
    return temp

#안전지대 세기
def count_safe(lab_map) :
    cnt = 0
    for i in range(len(lab_map)) :
        for j in range(len(lab_map[0])) :
            if lab_map[i][j] == 0 :
                cnt += 1
    return cnt

n, m = map(int, input().split())
lab_map = []
virus = deque()
for i in range(n) :
    row = list(map(int, input().split()))
    lab_map.append(row.copy())
    for j in range(len(row)) :
        if row[j] == 2 :
            virus.append((i, j))

# 0값 저장
zeros = deque()
for i in range(n) :
    for j in range(m) :
        if lab_map[i][j] == 0 :
            zeros.append((i, j))

walls = combinations(zeros, 3)
count = 0

for wall in walls :
    virus_cpy = copy.deepcopy(virus)
    answer = diffusion(build_wall(lab_map, wall), virus_cpy)
    count = max(count, count_safe(answer))
    
print(count)


