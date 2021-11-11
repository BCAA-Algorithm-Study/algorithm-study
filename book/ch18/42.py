# input setting
import sys
input = sys.stdin.readline
g = int(input())
p = int(input())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (g+1)
indegree = [1] * (g+1)

for i in range(1,g+1):
    parent[i] = i

airplane = []
for i in range(p):
    airplane.append(int(input()))

for max_gate in airplane:
    gate = find_parent(parent, max_gate)
    indegree[gate] -= 1
    union_parent(parent, gate, gate-1)
