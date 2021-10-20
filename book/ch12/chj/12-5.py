"""
뱀
"""
import sys, copy
from collections import deque
# import pprint
# pp = pprint.PrettyPrinter(indent=1)

input = sys.stdin.readline
# n = 10
# k = 4
# apple = [(1,2), (1,3), (1,4), (1,5)]
# l = 4
# direction = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]

# board = [[0] * n for _ in range(n)] # 사과: 5
# for i, j in apple:
#     board[i-1][j-1] = 5


n = int(input()) # board size
board = [[0] * n for _ in range(n)]

k = int(input()) # 사과 개수
for _ in range(k):
    i, j = map(int, input().split())
    board[i-1][j-1] = 5

l = int(input()) # 방향 전환 횟수
direction = []
for _ in range(l):
    x, c = input().split()
    direction.append((int(x), c))

second = 0
move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오른쪽, 아래, 왼쪽, 위(0, 1, 2, 3)
cur_dir = 0

def change_direction(cur_dir, dir):
    if dir == "D":
        return (cur_dir + 1) % 4
    if dir == "L":
        return (cur_dir - 1) % 4

snake = deque([[0,0]])
while True:
    # pp.pprint(board)
    # 이동
    head = snake[-1]
    x, y = head
    dx, dy = move[cur_dir]
    nx = x + dx
    ny = y + dy

    # 대가리를 벽과 부딪힌 경우
    if nx < 0 or ny < 0 or nx > n-1 or ny > n - 1:
        # print("벽에 부딪힘")
        break

    # 자기 몸통과 부딪힌 경우
    if [nx, ny] in snake:
        # print("몸에 부딪힘")
        break

    # 사과를 먹은 경우
    if board[nx][ny] == 5:
        board[nx][ny] = 0
    else:
        snake.popleft()

    

    snake.append([nx, ny])
    second += 1

    # 뱀 그리기 (임시)
    # temp = copy.deepcopy(board)
    # for x, y in snake:
    #     temp[x][y] = 1
    # print(second, "second")
    # pp.pprint(temp)
    # 방향 전환
    for x, c in direction:
        if second == x:
            cur_dir = change_direction(cur_dir, c)

print(second + 1)