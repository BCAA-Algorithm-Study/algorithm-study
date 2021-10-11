import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())
start = int(input())

graph = [[] for i in range(n+1)]

visited = [False] * (n+1)

distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    
    visited[start] = True
    distance[start] = 0

    for node, dist in graph[start]:
        distance[node] = dist
    
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for node, dist in graph[now]:
            cost = distance[now] + dist
            if cost < distance[node]:
                distance[node] = cost
    
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
