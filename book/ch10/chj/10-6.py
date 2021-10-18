"""
위상정렬
"""

from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []

    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            
            if indegree[next] == 0:
                q.append(next)

    print(result)

topology_sort()