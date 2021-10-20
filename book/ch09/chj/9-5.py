""" 전보 """

import sys
import heapq

INF = int(1e9)

input = sys.stdin.readline

n, m, start = map(int , input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))

def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for j in graph[now]:
            # j[0]: node, j[1]:cost
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(start)
max_cost = max([path[1] for path in graph[start]])
city = len(graph[start])

print(max_cost, city)