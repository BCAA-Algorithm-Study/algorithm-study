import sys

input = sys.stdin.readline

n = int(input())
target = int(input()) # target 후보
candidates = [int(input()) for _ in range(n-1)] # 나머지 후보
result = 0

if len(candidates) > 0 :
    while (target <= max(candidates)):
        first = candidates.index(max(candidates))
        target += 1
        candidates[first] -= 1
        result += 1

# print(target, candidates)
print(result)
