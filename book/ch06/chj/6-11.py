"""
성적이 낮은 순서로 학생 출력하기
"""

import sys

readline = sys.stdin.readline

n = int(input())

student = []

for _ in range(n):
    name, score = input().split()
    student.append((name, int(score)))

student.sort(key=lambda s : s[1])

for s in student:
    print(s[0], end=" ")
