import bisect
# input setting
import sys
n, x = map(int,sys.stdin.readline().rstrip().split())
nums = list(map(int,sys.stdin.readline().rstrip().split()))

l = bisect.bisect_left(nums, x)
r = bisect.bisect_right(nums, x)

count = r-l

if count == 0: 
    print(-1)
else:
    print(count)