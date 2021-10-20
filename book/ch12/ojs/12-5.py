import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

board = [[0]*n for _ in range(n)]
for i in range(k):
    r, c = map(int, sys.stdin.readline().split())
    board[r-1][c-1] = 1

l = int(sys.stdin.readline())
lst = []
for i in range(l):
    x, c = sys.stdin.readline().strip().split()
    x = int(x)
    lst.append((x,c))

seconds = 0
gameover = False
dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = 0
t=0
headx=0
heady=0
snake = deque([(headx, heady)])
# print(board)
for a in lst:
    x, c = a
    dd = d%4
    while t<x:
        t+=1
        seconds += 1
        headx += dx[dd]
        heady += dy[dd]
        if 0<=headx<n and 0<=heady<n and (headx, heady) not in snake:
            snake.append((headx,heady))
            if board[headx][heady] == 0:
                snake.popleft()
            else:
                board[headx][heady] = 0
        else:
            gameover = True
            break
        
        # print(f't:{t}, dir:{dd}')
        # print(f'head: ({headx},{heady})')
        # print(f'snake: {snake}')
        
    if gameover:
        break
    if c == 'L':
        d+=3
    else:
        d+=1

while not gameover:
    dd = d%4
    seconds += 1
    headx += dx[dd]
    heady += dy[dd]
    if 0<=headx<n and 0<=heady<n and (headx, heady) not in snake:
        snake.append((headx,heady))
        if board[headx][heady] == 0:
            snake.popleft()
    else:
        gameover = True
        break
print(seconds)