"""
만들 수 없는 금액
"""
import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
coins = list(map(int, input().split()))

currency = [False] * (sum(coins) + 1)
currency[sum(coins)] = True

for i in range(1, n):
    for per in list(permutations(coins, i)):
        currency[sum(per)] = True

for i in range(1, len(currency)):
    if currency[i] == False:
        print(i)
        break