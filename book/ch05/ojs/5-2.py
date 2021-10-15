import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

q = deque([(0, 0)])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while q:
    cx, cy = q.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            graph[nx][ny] += graph[cx][cy]
            q.append((nx,ny))

print(graph[n-1][m-1])