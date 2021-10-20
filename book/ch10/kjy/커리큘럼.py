import sys
from collections import deque
import copy

input = sys.stdin.readline

n = int(input())

indegree = [0] * (n + 1)
graph = [[] * (n + 1)]
endtime = [0] * (n + 1)

for i in range(1, n+1):
    now = map(int, input().split())
    graph[now[0]].extend(now[1:-1])
    indegree[i] = len(graph[now[0]])
    endtime[i] = now[0]


def topology_sort():
    result = copy.deepcopy(endtime)

    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + endtime[i])
            indegree -= 1
            if indegree == 0:
                q.append(i)
    print(max(endtime))
