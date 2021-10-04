
# n = int(input())
n = 3
array = []
# for _ in range(n):
#     array.append(int(input()))
array = [15, 27, 12]

#
array.sort(reverse=True)

# for i in array:
#     print(i, end=' ')

# ------------------------------------------
n = 3 
array = [15, 27, 12]
_temp = [0] * 100001

for x in array:
    _temp[x] += 1

_nums = []
for x in range(len(_temp)):
    for i in range(_temp[x]):
        _nums.append(x)

for i in _nums[::-1]:
    print(i, end=' ')
