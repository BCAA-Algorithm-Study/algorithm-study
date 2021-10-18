import copy

def rotate(key):
    l = len(key)
    new_key = [[0]*(l) for _ in range(l)]
    for i in range(l):
        for j in range(l):
            new_key[j][l-1-i] = key[i][j]
    return new_key        

def solution(key, lock):
    answer = True
    rotated_key = key
    l = len(lock)
    padded_lock = [[0]*(l+(l-1)*2) for _ in range(l+(l-1)*2)]
    for i in range(l-1, l+l-1):
        for j in range(l-1, l+l-1):
            padded_lock[i][j] = lock[i-(l-1)][j-(l-1)]
    
    padded_l = l+(l-1)*2
    key_l = len(key)
    rotated_key = key

    for i in range(4):
        # print(rotated_key)
        r=0
        while r<padded_l - key_l+1:
            c=0
            while c<padded_l - key_l+1:
                # print(r, c)
                lock_copy = copy.deepcopy(padded_lock)
                for a in range(key_l):
                    for b in range(key_l):
                        lock_copy[r+a][c+b] += rotated_key[a][b]
                # print(lock_copy)
                flag=True
                for a in range(l-1, l+l-1):
                    for b in range(l-1, l+l-1):
                        if lock_copy[a][b] != 1:
                            flag = False
                            break
                    if not flag:
                        break
                if flag: 
                    return True
                c+=1
            r+=1
        rotated_key = rotate(rotated_key)
                
    return False