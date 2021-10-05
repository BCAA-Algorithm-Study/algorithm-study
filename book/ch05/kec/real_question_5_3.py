def dfs(graph, x, y) :
    if x < 0 or y < 0 or x >= N or y >= M :
        return False
    elif graph[x][y] == 1:
        return False
    else :
        graph[x][y] = 1
        dfs(graph, x - 1, y)
        dfs(graph, x + 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x, y + 1)
        return True

N, M = map(int, input().split())
graph = []
for i in range(N) :
    graph.append(list(map(int, input())))
# print(graph)

cnt = 0
for x in range(N) :
    for y in range(M) :
        if dfs(graph, x, y) :
            cnt += 1
print(cnt)
