"""
개미전사
"""
import sys

input = sys.stdin.readline

n = int(input())
warehouse = list(map(int, input().split()))

dp = [0] * 100

dp[0] = warehouse[0]
dp[1] = max(warehouse[1], warehouse[0])

for i in range(2, n):
    dp[i] = max(dp[i-2] + warehouse[i], dp[i-1])

print(dp[n-1])
