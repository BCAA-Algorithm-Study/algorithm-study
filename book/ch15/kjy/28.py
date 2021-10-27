# input setting
import sys
import bisect

n = map(int,sys.stdin.readline().rstrip().split())
array = list(map(int,sys.stdin.readline().rstrip().split()))

l = 0
r = len(array)-1
mid = (l + r)//2
while l<=r and mid != array[mid]:
    mid = (l + r)//2 
    print(l, r, mid)
    if mid > array[mid]:
        l = mid+1
    elif mid < array[mid]:
        r = mid-1
        
if mid != array[mid]:
    print(-1)
else:
    print(mid)