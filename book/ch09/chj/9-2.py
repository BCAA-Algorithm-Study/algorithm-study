"""
Dijkstra with heapq
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int , input().split())

start = int(input())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = [] # 우선순위 큐로 사용하기위한 리스트

    heapq.heappush(q, (0, start)) # cost, node(start) 시작 노드 비용 0으로 heap push

    while q: # 우선순위 q가 비어있을때까지 반복
        dist, now = heapq.heappop(q)

        if distance[now] < dist: # distance table에 있는 거리가 더 적다면 업데이트 필요없음
            continue

        for i in graph[now]: # 이번 노드(now)와 연결된 node들 모두 탐색
            cost = dist + i[1] # 연결된 노드의 비용은 현재 노드(now)의 비용 + now와 연결된 해당 노드의 비용

            if cost < distance[i[0]]: # 비용이 이번 node를 거쳐 가는 비용이 더 적다면 업데이트
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0])) # 새롭게 발견한 경로이므로 heappush
                
dijkstra(start)

for i in range(1, n + 1):
    if distance == INF:
        print("INFINITY")
    else:
        print(distance[i])
        