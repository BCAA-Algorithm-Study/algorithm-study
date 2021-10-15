import sys
import heapq

n, m, c = map(int, sys.stdin.readline().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
dist[c] = 0

for i in range(m):
    x,y,z = map(int, sys.stdin.readline().split())
    graph[x].append((y,z))

h=[]
heapq.heappush(h, (0, c))
visited = [False]*(n+1)

while h:
    d, now = heapq.heappop(h)
    
    if visited[now]:
        continue
    visited[now] = True
    
    for nx, nd in graph[now]:
        if d + nd < dist[nx]:
            dist[nx] = d+nd
            heapq.heappush(h, (d+nd, nx))

cnt = 0
max_dist = -1
for i in dist:
    if i != INF:
        cnt += 1
        max_dist = max(max_dist, i)

print(cnt-1, max_dist)