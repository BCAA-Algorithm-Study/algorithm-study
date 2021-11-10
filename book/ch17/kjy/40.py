# input setting
import sys
import heapq
input = sys.stdin.readline
n, m = map(int,input().split())
INF = 1e9
graph = [[]*(n+1) for _ in range(n+1)]
distance = [INF] * (n+1)
distance[1] = 0
visited = []

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = [[0, 1]]

while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue
    for adj_node in graph[node]:
        cost = dist + 1
        if cost < distance[adj_node] and adj_node not in visited:
            distance[adj_node] = cost
            heapq.heappush(q,[cost, adj_node])
print(distance)
maximum = max(distance[1:])
number = distance.index(maximum)
count = distance.count(maximum)
print(number, maximum, count)