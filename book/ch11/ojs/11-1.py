import sys
from collections import deque

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

lst.sort()
q = deque(lst)

cnt = 0
while q:
    a = q.popleft()

    flag=0
    i = 1
    while i < a:
        if q:
            b= q.popleft()
            if b > a:
                a=b
        else:
            flag=1
            break
        i+=1
    if flag==0:
        cnt += 1
print(cnt)