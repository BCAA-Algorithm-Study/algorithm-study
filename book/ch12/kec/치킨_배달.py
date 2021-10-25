# https://www.acmicpc.net/problem/15686
from itertools import combinations


n, m = map(int, input().split())
inf = int(1e9)

home = []
chickens = []
city_map = [[0] * n for _ in range(n)]

for i in range(n) :
    temp = list(map(int, input().split()))
    for j in range(n) :
        if temp[j] == 1 :
            home.append((i, j))
        elif temp[j] == 2 :
            chickens.append((i, j))

array = combinations(chickens, m)
result = inf
for cks in array :
    tmp = [inf] * len(home)
    for r_ck, c_ck in cks :
        for i in range(len(home)) :
            r_h, c_h = home[i]
            tmp[i] = min(tmp[i], abs(r_ck - r_h) + abs(c_ck - c_h))
    result = min(result, sum(tmp))

print(result)
        

