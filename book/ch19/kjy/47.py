# input setting
import sys
from collections import deque
input = sys.stdin.readline

fish_array = []
fish_direction = []
min_fish = 1
direction = {1:[-1,0], 2: [-1,-1], 3: [0,-1], 4: [1,-1], 5:[1,0], 6:[1,1],7:[0,1],8:[-1,1]}
for i in range(4):
    temp = list(map(int,input().split()))
    fish_array.append(temp[4:])
    fish_direction.append(temp[:4])

def move_fish(fish_array, fish_direction):
    for i in range(16):
        # find i.th fish
        current_x, current_y = -1, -1
        if min_fish > i:
            continue
        for j in range(4):
            for k in range(4):
                if fish_array[j][k] == i:
                    current_x, current_y = j, k
        if current_x == -1 and current_y == -1: # 상어한테 해당 물고기가 먹혔을 경우
            continue
        
        next_x, next_y = -1,-1

        while True: 
            
            dx, dy = direction[fish_direction[current_x][current_y]]
            next_x, next_y = current_x + dx, current_y + dy
            if 0<=next_x<4 and 0<=next_y<4 and fish_array[next_x][next_y] != -1: # shark 위치 : -1
                fish_array[current_x][current_y], fish_array[next_x][next_y] = fish_array[next_x][next_y], fish_array[current_x][current_y]
                break
            else:
                fish_direction[current_x][current_y] += 1
                if fish_direction[current_x][current_y] > 8:
                    fish_direction[current_x][current_y] -= 8


eat_count = fish_array[0][0]
fish_array[0][0] = -1 # shark 위치

q = deque([[0,0,eat_count,fish_array,fish_direction]])
answer = []
while q:
    shark_x, shark_y, eat_count, temp_fish_array, temp_fish_direction = q.popleft()
    print(shark_x, shark_y, fish_direction)
    move_fish(temp_fish_array, temp_fish_direction) 
    next_x, next_y = -1,-1
    while True :
        dx, dy = direction[fish_direction[shark_x][shark_y]]
        next_x, next_y = shark_x + dx, shark_y + dy
        if 0<=next_x<4 and 0<=next_y<4:
            temp2 = temp_fish_array[next_x][next_y]
            temp_fish_array[next_x][next_y] = -1
            q.append(next_x, next_y, eat_count + fish_array[next_x][next_y], temp_fish_array, temp_fish_direction)
            temp_fish_array[next_x][next_y] = temp2
            shark_x, shark_y = next_x, next_y
        else:
            answer.append(eat_count)
            break

print(max(answer))