"""
커리큘럼
"""
import sys, copy
from collections import deque

input = sys.stdin.readline

v = int(input())

indegree = [0] * (v + 1)
time = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
    
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
        
    while q:
        now = q.popleft()

        for next in graph[now]:
            result[next] = max(result[next], result[now] + time[next])
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    for i in range(1, v+ 1):
        print(result[i])

topology_sort()