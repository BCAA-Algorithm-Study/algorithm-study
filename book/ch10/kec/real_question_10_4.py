import deque

N = int(input())
times = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
q= deque()

for i in range(1, N + 1) :
    temp = list(map(int, input().split()))
    times[i] = temp[0]

    if len(temp) > 2 :
        for precourse in temp[1 : -1] :
            graph[precourse].append(i)
            indegree[i] += 1
    else :
        q.append(i)

while q :
    now = q.popleft()
    for i in graph[now] :
        times[i] = 
