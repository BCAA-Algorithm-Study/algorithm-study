"""
모험가 길드
"""

import sys
input = sys.stdin.readline

n = int(input())
fears = list(map(int, input().split()))
fears.sort()
groups = 0

group = 0
for fear in fears:
    group += 1
    if group >= fear:
        groups += 1
        group = 0

print(groups)