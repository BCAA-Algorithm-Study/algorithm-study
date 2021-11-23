# input setting
import sys
import heapq
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
        find_parent(parent,b)
    else:
        parent[a] = b
        find_parent(parent,a)


n = int(input())
array = []
for i in range(n):
    temp = [i] + list(map(int,input().split()))
    array.append(temp)

array_x = sorted(array, key = lambda x:x[1])
array_y = sorted(array, key = lambda x:x[2])
array_z = sorted(array, key = lambda x:x[3])
parent = list(range(n))
cost = 0

q = []
for array_temp in [array_x,array_y,array_z]:
    for i in range(n-1):
        num1, x1, y1, z1 = array_temp[i]
        num2, x2, y2, z2 = array_temp[i+1]
        dist = min(abs(x1-x2),abs(y1-y2),abs(z1-z2))
        heapq.heappush(q, [dist, num1, num2] )

while q:
    dist,a,b = heapq.heappop(q)
    if find_parent(parent,a) == find_parent(parent,b):
        continue
    union_parent(parent,a,b)
    cost+=dist


print(cost)

