n, m = map(int,input('M N 공백으로 구분하여 입력').split())

# 얼음 틀
graph = list()
for _ in range(n):
    graph.append(list(map(int,input())))

# 본 문제

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 2
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False


cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            cnt+=1

print(cnt)
for k in graph:
    print(k)