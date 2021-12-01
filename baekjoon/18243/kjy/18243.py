# input setting
import sys
import pprint
input = sys.stdin.readline
n, k = map(int,input().split())
INF = 1e9
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0
# pprint.pprint(graph,width=600)
for i in range(k):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# pprint.pprint(graph,width=600)
def floid():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+ graph[k][j])
    # pprint.pprint(graph,width=600)
    for i in range(1, n+1):
        if any(graph[i][j]>6 for j in range(1, n+1)):
            print('Big World!')
            return 
    print('Small World!')
    return
floid()