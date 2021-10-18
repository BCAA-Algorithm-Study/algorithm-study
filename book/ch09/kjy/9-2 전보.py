import heapq

n, m, c = map(int, input().split())

INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b,d))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for node, d in graph[now]:
            cost = dist + d
            if distance[node] > cost:
                distance[node] = cost
                heapq.heappush(q,(cost,node))

dijkstra(c)

total_time = 0
count = 0 
for i in range(1, n+1):
    if distance[i] != INF:
        count +=1
        if distance[i] > total_time:
            total_time = distance[i]

print(count, total_time)
    


