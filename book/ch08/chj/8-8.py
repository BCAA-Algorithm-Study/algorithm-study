import sys

input = sys.stdin.readline

n, m = map(int, input().split())

coins = []
d = [10001] * (m + 1)
d[0] = 0

for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for i in range(coin, m + 1):
        if d[i -  coin] != 10001:
            d[i] = min(d[i], d[i - coin] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])


