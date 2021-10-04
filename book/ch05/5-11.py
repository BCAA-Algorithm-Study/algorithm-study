import pprint

def dfs(matrix, i, j, distance):
    if i in range(len(matrix)) and j in range(len(matrix[i])) and matrix[i][j] == 1:
        matrix[i][j] += distance
        pprint.pprint(matrix)
    else:
        return
    
    dfs(matrix, i+1,j,distance + 1)
    dfs(matrix, i-1,j,distance + 1)
    dfs(matrix, i,j+1,distance + 1)
    dfs(matrix, i,j-1,distance + 1)



def solution(N, M, matrix):
    dfs(matrix, 0, 0, 0)
    return matrix[N-1][M-1]

matrix = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

print(solution(5,6,matrix))