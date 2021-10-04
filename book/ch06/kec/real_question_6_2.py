nums = int(input())
nums_list = []
for i in range(nums) :
    nums_list.append(int(input()))
nums_list.sort(reverse = True)
print((' ').join(map(str, nums_list)))