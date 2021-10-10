import sys
from collections import deque

n = int(sys.stdin.readline())

indegree = [0]*(n+1)
t = [0]*(n+1)
cost = [[]]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    l = list(map(int, sys.stdin.readline().split()))
    t[i] = l[0]
    pre = l[1:-1]
    for p in pre:
        graph[p].append(i)
        indegree[i] += 1

def topology_sort():

    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    # print(f'q:{q}')
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            cost[i].append(t[now])
            # print(cost)
            if indegree[i] == 0:
                q.append(i)
                t[i] += max(cost[i])
topology_sort()
# print(cost)
print(t)