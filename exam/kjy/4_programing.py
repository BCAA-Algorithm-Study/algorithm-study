"""N x N 정사각형 격자에서 다음과 같은 룰을 가진 게임을 합니다.

최 좌측 상단(0, 0)에서 출발해서 최 우측 하단(N - 1, N - 1)에 도착하여야 합니다.

1-1. (a, b) = (행 번호, 열 번호)입니다.

인접한 칸들 중에서, 오른쪽 혹은 아래쪽 칸으로만 이동할 수 있습니다.

격자의 바깥으로는 벗어날 수 없습니다.

방문한 칸에 적힌 숫자만큼 점수를 획득합니다.

0 이 적힌 칸을 방문하면, 현재까지 획득한 점수에 -1을 곱할 수 있습니다. 즉, 부호를 바꿀 수 있습니다.

5-1. 부호를 바꾸지 않고, 그대로 유지하여도 괜찮습니다.

(N-1, N-1)에 도착했을 때, 획득한 점수를 가능한 크게 하는 것이 게임의 목적입니다.

아래 그림은 5 x 5 크기의 격자에서 최대 점수를 획득하는 경로를 나타냅니다.
(0, 0)에서 출발해서(4, 4)에 도착하여야 합니다.
격자에 0이 적힌 파란 칸에서는, 그 칸을 방문할 때까지 획득한 점수의 부호를 바꿀 수 있습니다.
처음 방문한 파란 칸(1, 2)까지 획득한 점수는 1 - 7 - 2 = - 8입니다. 여기서 부호를 바꾸기로 하면, 누적 점수는 8로 바뀝니다.
두 번째로 방문한 파란 칸(3, 3)까지 획득한 점수는 8 + 6 - 1 = 13입니다. 여기서 부호를 바꾸지 않기로 하면, 누적 점수는 그대로 13입니다.
최종 도착 칸(4, 4)까지 획득한 점수는 13 + 4 + 1 = 18입니다.
격자의 상태 board가 매개변수로 주어집니다. 위에 주어진 룰에 따라 게임을 진행한다고 했을 때, 얻을 수 있는 최대 점수를 return 하도록 solution 함수를 완성해주세요.

제한사항
board는 행의 길이와 열의 길이가 같은 2차원 정수형 배열입니다.
board의 행의 길이(=열의 길이)는 2 이상 1,000 이하입니다.
board의 모든 원소는 -10,000 이상 10,000 이하인 정수입니다.
즉, 격자 칸의 숫자는 -10,000 이상 10,000 이하인 정수입니다.
board의 행의 길이를 N이라고 하면, board[0][0]과 board[N-1][N-1]에는 항상 0이 아닌 값이 저장되어 있습니다.
##### 입출력 예

board	result
[[1, -7, -2, 1, -1],[2, 3, 0, -1, -2],[1, -1, 6, -1, -2],[-1, 1, -2, 0, 4],[-10, 5, -3, -1, 1]]	18
[[-10, 20, 30],[-10, 0, 10],[-20, 40, 1]]	61

[
[1, -7, -2, 1, -1],
[2, 3, 0, -1, -2],
[1, -1, 6, -1, -2],
[-1, 1, -2, 0, 4],
[-10, 5, -3, -1, 1]]	
18

[
[-10, 20, 30],
[-10, 0, 10],
[-20, 40, 1]]	61
"""
import copy
    
def solution(board):

    dx = [0,1]
    dy = [1,0]
    n = len(board)
    result = []
    def dfs(count, i, j, visited):
        if i < 0 or i >= n or j < 0 or j >= n or [i,j] in visited:
            return 
        elif i == n-1 and j == n-1:
            result.append(count+board[n-1][n-1])
            return

        temp_count = copy.deepcopy(count)
        temp_visited = copy.deepcopy(visited)
        temp_visited.append([i,j])
        number = board[i][j]
        if number == 0:
            for k in range(2):
                dfs(temp_count, i+dx[k], j+dy[k],temp_visited)
                dfs(-temp_count, i+dx[k], j+dy[k],temp_visited)
        else:
            for k in range(2):
                dfs(temp_count+number, i+dx[k], j+dy[k],temp_visited)
    dfs(0, 0, 0,[])

    return max(result)

if __name__ == '__main__':
    print(solution([[1, -7, -2, 1, -1],[2, 3, 0, -1, -2],[1, -1, 6, -1, -2],[-1, 1, -2, 0, 4],[-10, 5, -3, -1, 1]]))
    print(solution([[-10, 20, 30],[-10, 0, 10],[-20, 40, 1]]))