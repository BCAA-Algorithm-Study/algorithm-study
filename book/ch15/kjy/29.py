# input setting
import sys

n, c = map(int,sys.stdin.readline().rstrip().split())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

array.sort()

l = 1
r = array[-1] - array[0]
answer = []
while l<=r:
    gap = (l+r)//2

    # gap에 따라 공유기 설치하기
    prev = array[0]
    install = [array[0]]
    for i in range(1, len(array)):
        if array[i] - prev >= gap:
            install.append(array[i])
            prev = array[i]
    
    # binary search
    if len(install) >= c:
        answer.append(gap)
        l = gap + 1
    else:
        r = gap - 1


print(max(answer))
