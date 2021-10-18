"""
럭키 스트레이트
"""

import sys
input = sys.stdin.readline

score = list(map(int, input().rstrip()))

mid = len(score) // 2

if sum(score[:mid]) == sum(score[mid:]):
    print("LUCKY")
else:
    print("READY")