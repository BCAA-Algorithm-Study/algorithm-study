# https://programmers.co.kr/learn/courses/30/lessons/60059

def rotation(a) :
    rows = len(a)
    columns = len(a[0])
    result = [[0] * rows for _ in range(columns)]
    for i in range(rows) :
        for j in range(columns) :
            result[j][rows - i - 1] = a[i][j]
        return result

def check(new_lock) :
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2) :
        for j in range(lock_length, lock_length * 2) :
            if new_lock[i][j] != 1 :
                return False
    return  True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n) :
        for j in range(n) :
            new_lock[i + n][j + n] = lock[i][j]

    for rotate in range(4) :
        key = rotation(key)
        for x in range(n * 2) :
            for y in range(n * 2) :
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock) == True :
                    return True

                for i in range(m) :
                    for j in range(m) :
                        new_lock[x + i][y + j] -= key[i][j]

    return False
