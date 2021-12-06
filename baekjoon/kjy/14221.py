from collections import deque
# input setting
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

INF = 1e9
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

p, q = map(int,input().split())


def dijkstra(start):
    q = deque([[0,start]])
    distances = [INF] * (n+1)
    distances[start] = 0

    while q:
        distance, node = q.popleft()
        if distance > distances[node]:
            continue
        for next_node, dist in graph[node]:
            cost = dist + distances[node]
            if distances[next_node] > cost:
                distances[next_node] = cost
                q.append([distances[next_node], next_node])
    return distances
            

house_node = list(map(int,input().split()))
q_node = list(map(int,input().split()))

minimum = INF
my_home = None
for start in house_node:
    distances = dijkstra(start)
    for node in q_node:
        if distances[node] < minimum:
            minimum = distances[node]
            my_home = start
print(my_home)