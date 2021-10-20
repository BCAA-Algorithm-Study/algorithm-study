from itertools import combinations
from collections import Counter
# input setting
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
counter = Counter(input())

# n, m =5,3
# counter = Counter('1 3 2 3 2')

result = n * (n-1) / 2
for number in counter:
    dup = counter[number]
    if number.isdigit() and dup > 0:
        result -= dup * (dup-1) / 2
print(int(result))
