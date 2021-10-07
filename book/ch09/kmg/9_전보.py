import heapq
INF = int(1e9)

n, m, start, load = 3, 2, 1, [[1,2,4], [1,3,2]]

grap = [[] for i in range(n+1)]
d = [INF]* (n+1)

for x, y, z in load:
    grap[x].append((y,z))

def dijkstra(start):
    q = []
