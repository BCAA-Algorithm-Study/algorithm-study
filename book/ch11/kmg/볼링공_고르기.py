
# n, m = map(int, input().split())
# nums = map(int, input().split())

# n, m, nums = 5, 3, [1,3,2,3,2]
n, m, nums = 8, 5, [1,5,4,3,2,4,5,2]

_count = 0
for x in range(n):
    temp = nums[x]
    for i in range(x+1, n):
        if temp != nums[i]:
            _count += 1 
print(_count)