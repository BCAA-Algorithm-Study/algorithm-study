from collections import deque
#import  input setting
import sys


n, m, k, x = map(int, sys.stdin.readline().rstrip().split())


distance = [-1] * (n+1)
graph = [[] for _ in range(n+1)]


for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()

    for node in graph[now]:
        if distance[node] == -1:
            distance[node] = distance[now] + 1
            q.append(node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)