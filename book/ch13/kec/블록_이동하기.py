# https://programmers.co.kr/learn/courses/30/lessons/60063
import copy
import pprint

def bfs(board, drone) :
    move = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    while drone :
        temp = copy.deepcopy(board)
        now = drone.pop(0)
        time = now.pop()
        r_0, c_0 = now[0]
        r_1, c_1 = now[1]
        time += 1
        for dr, dc in move[:4] :  # 회전하지 않고 이동
            r_l = r_0 + dr
            r_r = r_1 + dr
            c_l = c_0 + dc
            c_r = c_1 + dc
            if 0 <= r_l < len(board) and 0 <= c_l < len(board) and 0 <= r_r < len(board) and 0 <= c_r < len(board) :
                if board[r_l][c_l] != 1 or board[r_r][c_l] != 1 :
                    drone.append([[r_l, c_l],[r_r, c_r], time])

        #회전이동   
        if r_0 == r_1 : # 가로 방향 일 때
            for dr, dc in move[4:] :
                if dc == 1 : # 오른쪽 좌표 고정
                    r_l = r_0 + dr
                    c_l = c_0 + dc
                    if 0 <= r_l < len(board) and 0 <= c_l < len(board) :
                        if board[r_l][c_0] != 1 and board[r_l][c_l] != 1 : # 회전 경로 모두 0 일때
                            r_min, r_max = sorted([r_l, r_1])
                            drone.append([[r_min, c_1], [r_max, c_1], time]) # 위쪽 좌표가 앞으로
                
                if dc == -1 : # 왼쪽 좌표 고정
                    r_r = r_1 + dr
                    c_r = c_1 + dc
                    if 0 <= r_r < len(board) and 0 <= c_r < len(board) :
                        if board[r_r][c_1] != 1 and board[r_r][c_r] != 1 : # 회전 경로 모두 0 일때
                            r_min, r_max = sorted([r_r, r_0])
                            drone.append([[r_min, c_1], [r_max, c_1], time]) # 위쪽 좌표가 앞으로
                            
        if c_0 == c_1 : # 세로 방향 일 때
            for dr, dc in move[4:] :
                if dr == -1 : # 아래쪽 좌표 고정
                    r_l = r_0 + dr
                    c_l = c_0 + dc
                    if 0 <= r_l < len(board) and 0 <= c_l < len(board) :
                        if board[r_0][c_l] != 1 and board[r_l][c_l] != 1 : # 회전 경로 모두 0 일때
                            c_min, c_max = sorted([c_l, c_1])
                            drone.append([[r_1, c_min], [r_1, c_max]]) # 왼쪽 좌표가 앞으로
                
                if dr == 1 : # 위쪽 좌표 고정
                    r_r = r_1 + dr
                    c_r = c_1 + dc
                    if 0 <= r_r < len(board) and 0 <= c_r < len(board) :
                        if board[r_0][c_r] != 1 and board[r_r][c_r] != 1 : # 회전 경로 모두 0 일때
                            r_min, r_max = sorted([c_r, c_0])
                            drone.append([[r_min, c_1], [r_max, c_1]]) # 위쪽 좌표가 앞으로
        
        board[r_0][c_0] = min(time, board[r_0][c_0])
        board[r_1][c_1] = min(time, board[r_1][c_1])
        pprint.pprint(board, width = 40)
        if temp == board :
            break

            
                    


    
def solution(board):
    drone = [[[0, 0], [0, 1], 1]]
    for i in range(len(board)) :
        for j in range(len(board)) :
            if board[i][j] == 0 :
                board[i][j] = 100
    bfs(board, drone)
    answer = board[-1][-1]
    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

print(solution(board))