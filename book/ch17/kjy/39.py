# input setting
import sys
import pprint
import heapq
import copy
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = []

t = int(input())
INF = 1e9

for i in range(t):
    n = int(input())
    
    array = []
    result = []
    visited = []
    for j in range(n):
        temp = list(map(int,input().split()))
        array.append(temp)
    distance = [[INF]*n for _ in range(n)]
    distance[0][0] = array[0][0]
    q = [[array[0][0], 0, 0]]
    while q:
        dist, i, j = heapq.heappop(q)
        if distance[i][j] < dist:
            continue
        for k in range(4):
            n_i, n_j = i+dx[k], j+dy[k]
            if n_i in range(n) and n_j in range(n):
                cost = dist + array[n_i][n_j]
                if cost < distance[n_i][n_j]:
                    distance[n_i][n_j] = cost
                    heapq.heappush(q,[distance[n_i][n_j],n_i,n_j])
    pprint.pprint(distance,width=30)
    answer.append(distance[-1][-1])

for i in range(t):
    print(answer[i])




