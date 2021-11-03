# input setting
import sys

n = int(input())
array = list(map(int,input().split()))
dp = [1] * (n+1)

for i in range(len(array)):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j]+1)


print(n-max(dp))