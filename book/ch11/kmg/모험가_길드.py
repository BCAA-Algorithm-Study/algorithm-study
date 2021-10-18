# n = int(input())
# x = map(int, input().spilt())

n = 5
x = [2,3,1,2,2]
n, x = 6, [1,2,3,4,5]

x.sort()
_sum = 0
count = 0
for i in x:
    _sum += i
    if _sum == 5:
        _sum = 0
        count +=1 
    elif _sum > 5:
        _sum = i
        count += 1

print(count)