import sys

n = int(sys.stdin.readline())
food = list(map(int, sys.stdin.readline().split()))

dp = [0]*n
dp[0] = food[0]
dp[1] = max(food[0], food[1])
for i in range(n):
    dp[i] = max(dp[i-2]+food[i], dp[i-1])
print(dp[-1])