num = int(input())
nums = []
for i in range(num) :
    nums.extend(list(map(int, input().split())))
    nums = sorted(nums, reverse = True)
    nums = nums[:num]

print(nums[-1])
