"""
볼링공 고르기
"""

import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())

balls = list(map(int, input().split()))
balls.sort()

result = 0

for i in range(len(balls)):
    for j in range(i+1, len(balls)):
        if balls[i] == balls[j]:
            continue
        else:
            result += 1

print(result)