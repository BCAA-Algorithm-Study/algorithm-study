# a(i) = max(a(i-2)+b(i), a(i-1))

# n = int(input())
# array = map(int, input().split())

n = 4
array = [0] + [1,3,1,5]

# DP 테이블
d = [0] * 100

for i in range(1, n+1):
    if i < 3:
        d[i] = array[i]
        continue
    d[i] = max(d[i-2]+array[i], d[i-1])
    # print(d[:i+1])
print(d[n])