from collections import deque

n,m= map(int,input().split())

MAP = list()
for i in range(n):
    MAP.append(list(map(int,input())))

dx = [0, 0,-1, 1]
dy = [1,-1, 0, 0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue: # queue가 비어있지 않는 동안
        x,y = queue.popleft()
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if MAP[nx][ny] == 0:
                continue

            if MAP[nx][ny] == 1:
                MAP[nx][ny]= MAP[x][y]+1
                queue.append((nx,ny))
                
    MAP[0][0]-=2
    return MAP[n-1][m-1]

print('***'*m)  
for k in MAP:
    print(k)
print('***'*m)    
print('answer:',bfs(0,0))
print('***'*m)  
for k in MAP:
    print(k)
print('***'*m)  