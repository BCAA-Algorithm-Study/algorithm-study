from collections import deque
import sys

inf = int(1e9)
n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
citys = [[] for _ in range(n + 1)]
distance = [inf] * (n + 1)
distance[x] = 0
visited = [False] * (n + 1)
now = deque()
now.append(x)

for _ in range(m) :
    start, end = map(int, sys.stdin.readline().rstrip().split())
    citys[start].append(end)


while now :
    start = now.popleft()
    visited[start] = True
    for i in citys[start] :
        if not visited[i] :
            now.append(i)
        distance[i] = min(distance[start] + 1, distance[i])

answer = [i for i in range(len(distance)) if distance[i] == k]

if not answer :
    print(-1)
else :
    for i in answer :
        print(i)
