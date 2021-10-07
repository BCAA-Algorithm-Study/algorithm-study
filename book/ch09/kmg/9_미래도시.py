n, m, x, k, a = 5, 7, 4, 5, [[1,2],[1,3],[1,4],[2,4],[3,4],[3,5],[4,5]]
n, m, x, k, a = 4, 2, 3, 4, [[1,3],[2,4]]



INF = int(1e9)
grap = [[INF]*(n+1) for _ in range(n+1)]

for t in range(n+1):
    grap[t][t]=0

for a, y in a:
    grap[a][y] = 1
    grap[y][a] = 1

for t in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            grap[a][b] = min(grap[a][b], grap[a][t] + grap[t][b])

d= grap[1][k] + grap[k][x]
if d > INF:
    print(-1)
else:
    print(d)
