# input setting
import sys
import pprint
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]


for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b],c)    
 
for i in range(1,n+1):
    graph[i][i] = 0
# print(graph)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
            # pprint.pprint(graph, width = 30)

for i in range(1,n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, n+1):
    print(*graph[i][1:])

# infinity 처리
