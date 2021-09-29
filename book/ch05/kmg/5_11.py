n, m = 5, 6

miro = [[1,0,1,0,1,0], 
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        ]

from collections import deque

temp = deque()
# (상, 하, 좌, 우)
dx = [-1, 1, 0,  0]
dy = [ 0, 0, -1, 1]

#### 
def dfs(x, y):
    temp = deque()
    temp.append((x,y))
    while temp:
        x, y = temp.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                temp.append((nx, ny))
            else:
                continue

    print(miro) # [[3, 0, 5, 0, 7, 0], [2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 8], [14, 13, 12, 11, 10, 9], [15, 14, 13, 12, 11, 10]]
    return miro[n-1][m-1]
print(dfs(0,0))
