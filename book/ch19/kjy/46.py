from collections import deque
# input setting
import sys
import pprint
input = sys.stdin.readline

n = int(input())
shark_size = 2
shark_eat = 0
array = []
answer = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(n):
    temp = list(map(int,input().split()))
    array.append(temp)
    # 시작 위치 찾기
    if 9 in temp:
        start_r, start_c = i, temp.index(9)

width = range(len(array))
height = range(len(array))
def find_fish(array, start_r, start_c):
    visited = []
    temp_fish = []
    nearest_dist = 1e9
    q = deque([[0, start_r, start_c]])
    while q:
        dist, current_x, current_y = q.popleft()
        for i in range(4):
            next_x, next_y = current_x + dx[i], current_y + dy[i]
            if next_x in width and next_y in height and [next_x, next_y] not in visited and array[next_x][next_y] <= shark_size:
                visited.append([next_x, next_y])
                q.append([dist+1, next_x, next_y])
                if 0 < array[next_x][next_y] < shark_size :
                    temp_fish.append([dist+1, next_x, next_y])
                    if nearest_dist >= dist+1:
                        nearest_dist = dist+1
        
    fish = []
    for dist,x,y in temp_fish:
        if dist == nearest_dist and dist < 1e9:
            fish.append([x,y,dist])
    fish.sort()
    return fish[0] if fish else None


while True:
    array[start_r][start_c] = 0
    result = find_fish(array, start_r, start_c)
    if not result:
        break  
    start_r, start_c, dist = result
    array[start_r][start_c] = 9
    # print(dist, shark_size, shark_eat)
    # pprint.pprint(array, width = 30)
    answer += dist
    shark_eat += 1
    if shark_size == shark_eat:
        shark_size += 1
        shark_eat = 0

print(answer)



    