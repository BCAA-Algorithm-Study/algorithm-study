import numpy as np
import copy

def rotation(array):
    l = len(array)
    temp = np.ones((l,l))
    for i in range(l):
        for j in range(l):
            temp[j][len(array) - i - 1] = array[i][j]
    return temp

            
def padding(key, lock, n, m):
    k = n+2*m-2
    padding = np.zeros((k,k))
    padding[m-1:m+n-1, m-1:m+n-1] = lock
    return padding


def solution(key, lock):
    answer = True
    key, lock = np.array(key), np.array(lock)
    count = 0
    n = len(lock)
    m = len(key)
    while count < 4:
        pad_array = padding(key, lock, n, m)
        for i in range(n+m-1):
            for j in range(n+m-1):
                check = copy.deepcopy(pad_array)
                check[i:i+m, j:j+m] += key
                print('key \n', key)
                print('check \n', check)
                print('lock \n', check[m-1:m+n-1, m-1:m+n-1])
                if np.all(check[m-1:m+n-1, m-1:m+n-1] == 1):
                    return True
                
        key = rotation(key)
        count +=1
    
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))