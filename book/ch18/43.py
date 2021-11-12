# input setting
import sys
import heapq

input = sys.stdin.readline
n, m = map(int,input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


q = []
parent = [0] * n
for i in range(1,n):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int,input().split())
    heapq.heappush(q, [c,a,b])

cost = 0
print(q)
while q:
    dist, a, b = heapq.heappop(q)
    if find_parent(parent, a) == find_parent(parent, b):
        cost+=dist
        continue
    print(a,b,parent,"!!!")
    union_parent(parent,a,b)
    print(parent)
    
    

print(cost)