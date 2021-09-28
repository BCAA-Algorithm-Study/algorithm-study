"""
<미로 탈출>
NxM 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를
피해 탈출해야 한다. 위치는 (1,1)이고 미로의 출구는 (N,M)의 위치에 존재하며
한번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은
1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 탈출하기
위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
"""
from collections import deque

n, m = map(int, input().split())

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

graph = []
for i in range(n):
   graph.append(list(map(int, input())))
   
def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= m or nx < 0 or ny < 0: # 범위를 벗어난 경우 제외
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1: # 처음 가보는 곳 발견
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]


print(bfs(0, 0))