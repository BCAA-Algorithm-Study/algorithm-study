import sys
n, m = map(int, sys.stdin.readline().split())
coins = []
dp = [99999]*(10001)
dp[0] = 0
for i in range(n):
    coin = int(sys.stdin.readline())
    dp[coin] = 1
    coins.append(coin)

coins.sort()

for i in range(coins[0], m+1):
    for c in coins:
        if c > i:
            break
        dp[i] = min(dp[i], dp[i-c]+1)
# print(dp)
if dp[m]==99999:
    print(-1)
else:
    print(dp[m])