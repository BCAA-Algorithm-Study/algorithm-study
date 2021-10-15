import sys
from collections import defaultdict

n, m =map(int,sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))

b = defaultdict(int)

for i in k:
    b[i]+=1

weights = list(b.keys())
weights.sort()

result=0
for i, w in enumerate(weights):
    cnt = 0
    for j in range(i+1, len(weights)):
        cnt += b[weights[j]]
    result += b[w] * cnt

print(result)