def dfs(graph, v, visted) :
    visted[v] = True
    print(v, end = ' ')
    for i in graph[v] :
        if not visted[i] :
            dfs(graph, i, visted)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)
