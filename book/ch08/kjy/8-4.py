# n, m = map(int,input())

# array = []
# for i in range(n):
#     array.append(int(input))

n, m =2,15
array = [2,3]

d = [10001] * (m+1)
d[0] = 0

for unit in array:
    for i in range(unit, len(d)):
            d[i] = min(d[i], d[i-unit] + 1)

print(d[m])