# https://www.acmicpc.net/problem/18428
import pprint
import copy
from itertools import combinations

def bfs(corridor, teacher) :
    temp = copy.deepcopy(corridor)
    view = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for r_t, c_t in teacher :
        for r_v, c_v in view :
            for i in range(1, n) :
                r_n = r_t + (r_v * i)
                c_n = c_t + (c_v * i)
                if 0 <= r_n < n and 0 <= c_n < n :
                    if temp[r_n][c_n] == 'O' :
                        break
                    if temp[r_n][c_n] == 'S' :
                        return False
                else : break
    return True


def check_view(corridor, teacher, obj) :
    for o in obj :
        temp = copy.deepcopy(corridor)
        for r_o, c_o in o :
            temp[r_o][c_o] = 'O'

        if bfs(temp, teacher) :
            # pprint.pprint(temp, width = 30)
            return 'YES'
    return 'NO'

n = int(input())
corridor = [[] for _ in range(n)]
teacher = []
X = []
obj = []
for i in range(n) :
    temp = list(input().split())
    corridor[i] =temp
    for j in range(n) :
        if temp[j] == 'T' :
            teacher.append((i, j))
        if temp[j] == 'X' :
            X.append((i, j))
obj = list(combinations(X, 3))

print(check_view(corridor, teacher, obj))
# print(list(obj))
#
# pprint.pprint(corridor, width = 30)
