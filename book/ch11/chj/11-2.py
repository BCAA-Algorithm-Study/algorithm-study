"""
곱하기 혹은 더하기
"""

import sys
input = sys.stdin.readline

S = list(map(int, list(input().rstrip())))
print(S)

for i in range(0, len(S)-1):
    if S[i] == 0 or S[i+1] == 0:
        S[i+1] = S[i] + S[i+1]
    else:
        S[i+1] = S[i] * S[i+1]

print(S[-1])