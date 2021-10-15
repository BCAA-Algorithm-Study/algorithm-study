import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

s = 0
e = max(lst)
mid = 0

while s <= e:
    mid = (s+e)//2
    total = 0
    for i in lst:
        if mid < i:
            total += i - mid
    if total == m:
        break
    elif total > m :
        s = mid + 1
    else :
        e = mid - 1

print(mid)