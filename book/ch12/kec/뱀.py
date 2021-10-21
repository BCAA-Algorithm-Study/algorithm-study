# https://www.acmicpc.net/problem/3190
import pprint
from collections import deque

n = int(input())

# 지도 만들기
array = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(n + 2) :
    array[0][i] = -1
    array[i][0] = -1
    array[i][-1] = -1
    array[n + 1][i] = -1


# 사과 위치 저장
k = int(input())
for i in range(k) :
    row, col = map(int, input().split())
    array[row][col] = 1

# pprint.pprint(array, width = 50)

# length = 1  # 뱀길이

# 이동방향 정의
direction_array = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0

# 뱀 위치 저장
snake = deque([(1, 1)])
time = 0
end = False
tail = None

move = []
l = int(input())
for i in range(l) :
    x, c = input().split()
    x = int(x)
    move.append((x, c))
move.append((101, 'L'))

for x, c in move :
    head_x, head_y = snake[-1] # 머리 위치
    dx, dy = direction_array[d]
    for i in range(time, x) : # 주어진 시간동안 머리방향으로 이동
        time += 1
        head_x += dx
        head_y += dy
        
        if array[head_x][head_y] == 1 : # 머리 위치에 사과가 있을 때
            array[head_x][head_y] = 0
            # length += 1
            
        else :
            tail = snake.popleft() # 꼬리 이동

        if array[head_x][head_y] == -1 or (head_x, head_y) in snake or tail == (head_x, head_y):
            print(time)
            # print(snake)
            # pprint.pprint(array, width = 50)
            end = True
            break
        else :
            snake.append((head_x, head_y))
        # print(snake)
    if end :
        break
    elif c.upper() == 'D' :
        d += 1
    elif c.upper() == 'L':
        d -= 1

    if d == 4 :
        d = 0
    elif d == -1 :
        d = 3
