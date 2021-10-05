n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(y, x):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    
    if graph[y][x] == 0:
        graph[y][x] = 1

        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x - 1)
        dfs(y, x + 1)

        return True

    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)