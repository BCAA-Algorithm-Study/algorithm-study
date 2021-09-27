import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

result = 0

for _ in range(n):
    pick = min(list(map(int, input().split())))
    result = max(result, pick)

print(result)