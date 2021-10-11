import heapq

INF = int(1e9)
N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
q = []
distance = [INF] * (N + 1)
distance[C] = 0
heapq.heappush(q, (0, C))

for _ in range(M) :
    a, b, time = map(int, input().split())
    graph[a].append((time, b))

while q :
     time, city = heapq.heappop(q)
     if distance[city] < time :
         continue
     for i in graph[city] :
         if time + i[0] < distance[i[1]] :
             distance[i[1]] = time + i[0]
             heapq.heappush(q, (time + i[0], i[1]))

count = 0
max_dist = 0
for i in distance :
    if 0 < i < INF :
        count += 1
        max_dist = max(max_dist, i)

print(count, max_dist)
