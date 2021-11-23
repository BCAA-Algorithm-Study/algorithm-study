'''
문제 설명
rows 행 columns 열로 나열되어 있는 트랜지스터들이 있습니다. 일부 상하좌우로 인접한 트랜지스터들 사이에는 회로가 연결되어 있습니다. 당신은 이 회로들의 일부분을 잘라내고자 합니다. 회로를 잘라내는 과정은 다음과 같습니다.

임의의 서로 다른 두 트랜지스터를 고른 뒤, 그 두 트랜지스터를 포함하면서 가장 작은 직사각형 영역의 겉테두리와 교차하는 모든 회로를 잘라냅니다.
예를 들어, 다음 그림은 트랜지스터들이 회로로 연결되어 있는 상태에서, 2행 2열과 3행 1열에 있는 두 트랜지스터를 고른 뒤 회로를 잘라내는 과정을 그린 것입니다.

cutexample.png

트랜지스터들이 배열된 행의 개수 rows, 열의 개수 columns, 초기 회로 연결상태를 나타내는 2차원 정수배열 connections, 그리고 회로을 잘라낼 영역들을 의미하는 2차원 정수배열 queries가 매개변수로 주어집니다. 매 영역마다 잘라지는 회로의 개수들을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

제한 사항
rows, columns는 각각 2 이상 50 이하인 자연수입니다.
connections의 길이는 1 이상 2 x rows x columns - rows - columns 이하입니다.
connections의 각 원소는 [r1, c1, r2, c2] 4개의 정수로 이루어져 있습니다. 이는 r1행 c1열의 트랜지스터와 r2행 c2열 트랜지스터 사이에 회로가 연결되어 있다는 의미입니다.
r1, r2는 1 이상 rows 이하입니다.
c1, c2는 1 이상 columns 이하입니다.
r1행 c1열과 r2행 c2열은 인접한 두 위치입니다.
모든 회로는 서로 다른 위치에 있습니다.
queries의 길이는 1 이상 100 이하입니다.
queries의 각 원소는 [r1, c1, r2, c2] 4개의 정수로 이루어져 있습니다. 이는 r1행 c1열의 트랜지스터와 r2행 c2열의 트랜지스터를 골라 회로를 잘라야 한다는 의미입니다.
r1, r2는 1 이상 rows 이하입니다.
c1, c2는 1 이상 columns 이하입니다.
두 트랜지스터는 서로 다른 트랜지스터입니다.
입출력 예
rows	columns	connections	queries	result
4	3	[[1,1,2,1],[1,2,1,3],[1,3,2,3],[2,2,2,3],[2,2,3,2],[2,3,3,3],[3,2,3,3],[3,2,4,2],[4,1,4,2]]	    [[2,2,3,1],[1,2,4,2]]	    [4,2]
2	2	[[1,1,1,2],[2,2,1,2],[2,1,1,1],[2,2,2,1]]	    [[1,1,2,2],[1,1,2,1],[2,1,2,2]]	    [0,2,2]
3	3	[[1,1,2,1],[2,1,3,1],[1,2,2,2],[2,2,3,2],[1,3,2,3],[2,3,3,3]]	    [[1,1,3,1],[1,2,3,2],[1,3,3,3]]     	[0,0,0]
입출력 예 설명
입출력 예 #1

주어진 입력을 그림으로 표현하면 다음과 같습니다.
ex1.png
처음에는 4개의 회로가 잘라지고, 그 다음에는 2개의 회로가 잘라지므로, [4,2]를 return 해야 합니다.
입출력 예 #2

주어진 입력을 그림으로 표현하면 다음과 같습니다.
ex2.png
처음에는 0개, 그 다음에는 2개, 마지막에도 2개의 회로가 잘라지므로, [0,2,2]를 return 해야 합니다.
입출력 예 #3

주어진 입력을 그림으로 표현하면 다음과 같습니다.
ex3.png
그 어떤 상황에서도 회로가 잘라지지 않았으므로, [0,0,0]을 return 해야 합니다.
'''
import copy

def solution(rows, columns, connections, queries):
    answer = []

    for query in queries :
        cnt = 0
        r_1, c_1, r_2, c_2 = query
        min_r, max_r = sorted([r_1, r_2])
        min_c, max_c = sorted([c_1, c_2])
        for row in range(min_r, max_r + 1) :  # 세로 연결 제거
            if [row, min_c, row, min_c - 1] in connections :
                connections.remove([row, min_c, row, min_c - 1])
                cnt += 1
            elif [row, min_c - 1, row, min_c] in connections :
                connections.remove([row, min_c - 1, row, min_c])
                cnt += 1

            if [row, max_c, row, max_c + 1] in connections :
                connections.remove([row, max_c, row, max_c + 1])
                cnt += 1
            elif [row, max_c + 1, row, max_c] in connections :
                connections.remove([row, max_c + 1, row, max_c])
                cnt += 1
        for col in range(min_c, max_c + 1) :  # 가로 연결 제거
            if [min_r, col, min_r - 1, col] in connections :
                connections.remove([min_r, col, min_r - 1, col])
                cnt += 1
            elif [min_r - 1, col, min_r, col] in connections :
                connections.remove([min_r - 1, col, min_r, col])
                cnt += 1

            if [max_r, col, max_r + 1, col] in connections :
                connections.remove([max_r, col, max_r + 1, col])
                cnt += 1
            elif  [max_r + 1, col, max_r, col] in connections :
                connections.remove([max_r + 1, col, max_r, col])
                cnt += 1
        answer.append(cnt)

    return answer

rows = 4
columns = 3
connections = [[1,1,2,1],[1,2,1,3],[1,3,2,3],[2,2,2,3],[2,2,3,2],[2,3,3,3],[3,2,3,3],[3,2,4,2],[4,1,4,2]]
queries = [[2,2,3,1],[1,2,4,2]]

solution(rows, columns, connections, queries)