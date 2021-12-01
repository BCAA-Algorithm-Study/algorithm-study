# input setting
import sys
import pprint
import heapq
input = sys.stdin.readline

tc = int(input())
INF = 1e9
answer = []


for _ in range(tc):
    N, M, W = map(int,input().split())
    road = [[INF] *(N+1) for _ in range(N+1)] 
    graph = [[] for _ in range(N+1)]
    for i in range(1,N+1):
        road[i][i]= 0
    for _ in range(M):
        a,b,c = map(int,input().split())
        if road[a][b] > c:
            road[a][b] = c
            road[b][a] = c

    
    for _ in range(W):
        a,b,c = map(int, input().split())
        if road[a][b] > -c:
            road[a][b] = -c
    
    for i in range(1,N+1):
        for j in range(1, N+1):
            if i!=j and road[i][j] != INF:
                graph[i].append([j, road[i][j]])

    def dijkstra(start):
        distance = [INF]*(N+1)
        q = []
        heapq.heappush(q,[0, start])

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue
            for node, d in graph[now]:
                cost = dist + d
                if cost < distance[node]:
                    distance[node] = cost
                    heapq.heappush(q,(cost, node))
        return distance[start]

    for i in range(1,N+1):
        result = dijkstra(i)
        if result < 0:
            answer.append('YES')
        else:
            answer.append('NO')
    # pprint.pprint(road,depth = 200)
for i in answer:
    print(i)




import copy
for _ in range(int(input())):
    n, m, w = map(int, input().split()) #node, load, worm

    INF = int(1e9)
    dist = [INF] * (n+1)

    loads = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, input().split()) #start, end, cost
        loads[s].append((e,t))
        loads[e].append((s,t))

    for _ in range(w):
        s, e, t = map(int, input().split()) #start, end, cost
        loads[s].append((e, -t))

    def bf(start, distance = []):
        distance = copy.deepcopy(dist)
        distance[start] = 0
        for i in range(n+1):
            for j in range(n+1):
                for end, cost in loads[j]:
                    if distance[end] > distance[j] + cost:
                        distance[end] = distance[j] + cost
                        if i == n:
                            return True
        return False

    if bf(1):
        print("YES")
    else:
        print("NO")
