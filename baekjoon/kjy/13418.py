# input setting
import sys
import copy
input = sys.stdin.readline
n, m = map(int,input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(a,b,parent):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n+1)]
edges=[]
for i in range(m+1):
    a, b, cost = map(int,input().split())
    if i == 0:
        union_parent(a,b,parent)
        result = int(cost==0)
        continue
    edges.append((cost,a,b))

edges.sort(reverse=True)

min_result = result
min_parent = copy.deepcopy(parent)
for cost, a, b in edges:
    if find_parent(min_parent, a) != find_parent(min_parent, b):
        union_parent(a,b,min_parent)
        if cost == 0:
            min_result+=1

edges.sort()
max_parent = copy.deepcopy(parent)
max_result = result
for cost, a, b in edges:
    if find_parent(max_parent, a) != find_parent(max_parent, b):
        union_parent(a,b,max_parent)
        if cost == 0:
            max_result+=1

print(max_result**2 - min_result**2)



