"""
자물쇠와 열쇠
"""
import sys
# import pprint
input = sys.stdin.readline

# pp = pprint.PrettyPrinter(indent=1)

def solution(key, lock):

    answer = False
    n, m = len(key), len(lock)
    # 확장된 map 생성
    extension = n + (m - 1) * 2
    ext_map = [[0] * extension for _ in range(extension)]

    center = extension//2 - n//2
    for i in range(n):
        for j in range(n):
            if key[i][j] == 1:
                ext_map[i+center][j+center] = 1
    
    for r in range(4): # rotate 90 
        # pp.pprint(ext_map)
        for i in range(extension - m + 1):
            for j in range(extension - m + 1):
                mat = []
                for k in range(m):
                    mat.append(ext_map[i+k][j:j+m])
                answer = compare(mat, lock)
                if answer:
                    return answer 
        ext_map = rotate(ext_map)
     
    return answer

def rotate(mat):
    rotated = [[0] * len(mat) for _ in range(len(mat))]
    length = len(mat)
    for i in range(len(mat)):
        for j in range(len(mat)):
            rotated[i][j] = mat[j][length - 1 - i]
    return rotated

def compare(key, lock):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == key[i][j]:
                return False
    return True

if __name__=="__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    print(solution(key, lock))