# n, m = map(int, input().split())
n, m  = 4, 5 

frame = [[0,0,1,0,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]

def find0(x, y):
    if x >= n or y >= m or x < 0 or y < 0:
        return False
    if frame[x][y] == 0:
        frame[x][y] = 1
        find0(x, y+1)   #
        find0(x+1, y)   #
        find0(x-1, y)   #
        find0(x, y-1)   #
        return True
    return False

answer = 0 
for x in range(n):
    for y in range(m):
        if find0(x, y) == True:
            answer += 1 
print(answer)
"""
4 5
00100
00011
11111
00000
"""