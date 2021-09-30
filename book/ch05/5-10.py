def dfs(matrix, i, j):
    if i in range(len(matrix)) and j in range(len(matrix[i])) and matrix[i][j] == 0:
        matrix[i][j] = 1
        
    else:
        return
    
    dfs(matrix, i+1,j)
    dfs(matrix, i-1,j)
    dfs(matrix, i,j+1)
    dfs(matrix, i,j-1)


def solution(matrix):
    
    answer = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0 :
                dfs(matrix, i, j)
                answer+=1

    return answer
    
matrix = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

print(solution(matrix))