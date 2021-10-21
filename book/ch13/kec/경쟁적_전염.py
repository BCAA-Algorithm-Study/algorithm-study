# https://www.acmicpc.net/problem/18405
from collections import deque
from pprint import pprint

def diffusion(test, virus_key, virus_list) :
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    length = len(virus_list)
    for i in range(length) :
        x, y = virus_list.popleft()
        for dx, dy in move :
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n :
                if  test[nx][ny] == 0 :
                    test[nx][ny] = virus_key
                    virus_list.append((nx, ny))

n, k = map(int, input().split())
test = [[] for _ in range(n)]
virus_dict = {}
for i in range(1, k + 1) :
    virus_dict[i] = deque()

for i in range(0, n) :
    test[i] = list(map(int, input().split()))
    for j in range(len(test[i])) :
        if test[i][j] != 0 :
            virus_dict[test[i][j]].append((i, j))

s, x , y = map(int, input().split())

for i in range(1, s + 1) :
    for k, v in virus_dict.items() :
        diffusion(test, k, v)


print(test[x - 1][y - 1])
