import sys

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

edges = []

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))

edges.sort()
total = 0
used_edge = []

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += c
        used_edge.append(c)

print(total - max(used_edge))