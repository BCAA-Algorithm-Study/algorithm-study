import heapq

INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1) :
    graph[i][i] = 0
for i in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1) :
    for a in range(1, N + 1) :
        for b in range(1, N + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            graph[b][a] = graph[a][b]

X, K = map(int, input().split())
# print(graph)
if (graph[1][K] + graph[K][X]) < INF :
    print(graph[1][K] + graph[K][X])
else :
    print(-1)
