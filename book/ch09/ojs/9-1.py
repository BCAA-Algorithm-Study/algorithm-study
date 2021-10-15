import sys

n, m = map(int, sys.stdin.readline().split())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, sys.stdin.readline().split())

for c in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

dist = graph[1][k] + graph[k][x]

if dist >= INF:
    print(-1)
else:
    print(dist)