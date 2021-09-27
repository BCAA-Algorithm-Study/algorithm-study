import sys

input = sys.stdin.readline

n, k = map(int, input().split())

result = 0

while n >= k:
    result += n % k
    result += 1
    n //= k

print(result)

