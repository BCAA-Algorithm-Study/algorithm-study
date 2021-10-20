import sys
import copy
from collections import deque
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())

graph = []
chicken = []
house = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    line2 = []
    for j, l in enumerate(line):
        if l==1:
            house.append((i,j))
        if l==2:
            chicken.append((i,j))
            line2.append(0)
            continue
        line2.append(l)
    graph.append(line2)

def get_chicken_len(h, c):
    hx, hy = h
    min_l = int(1e9)
    for coord in c:
        cx, cy = coord
        l = abs(hx-cx) + abs(hy-cy)
        min_l = min(min_l, l)    
    return min_l

case = list(combinations(chicken, m))

min_chicken_len = int(1e9)
for c in case:
    city_chicken_len = 0
    for h in house:
        x, y = h
        city_chicken_len += get_chicken_len(h, c)
    min_chicken_len = min(min_chicken_len, city_chicken_len)
    
    

print(min_chicken_len)