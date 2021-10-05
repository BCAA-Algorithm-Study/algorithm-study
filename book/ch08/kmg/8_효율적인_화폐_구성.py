# n, m = list(map(int, input().split()))
# array = []
# for _ in range(n):
#     array.append(int(input()))
n, m , array = 2, 15, [2,3] # return: 5
# n, m , array = 3, 4, [3,5,7] # return: -1

d = [-1] * 10001
for x in array:
    d[x] = 1

for i in range(0, m+1):
    
