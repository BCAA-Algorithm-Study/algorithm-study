import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
    if i == 0:
        q = list(map(int, input().split()))
    else:
        for k in map(int, input().split()):
            heapq.heappush(q, k)
            heapq.heappop(q)
print(q[0])