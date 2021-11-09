# input setting
import sys
import pprint
input = sys.stdin.readline

n, m = map(int,input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
graph1 = [[INF]*(n+1) for _ in range(n+1)]
graph2 = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph1[a][b] = 1
    graph2[b][a] = 1

for i in range(1,n+1):
    graph1[i][i] = 0
    graph2[i][i] = 0

# pprint.pprint(graph,width = 100)

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph1[i][j] = min(graph1[i][j], graph1[i][k] + graph1[k][j])
            graph2[i][j] = min(graph2[i][j], graph2[i][k] + graph2[k][j])
    
count = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        graph[i][j] = min(graph1[i][j],graph2[i][j])

for i in range(n):
    if INF not in graph[i][1:]:
        count+=1
print('graph1')
pprint.pprint(graph1,width = 100)
print('graph2')
pprint.pprint(graph2,width = 100)

print(count)