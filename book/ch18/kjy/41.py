# input setting
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

array = []
for i in range(n):
    temp = list(map(int,input().split()))
    array.append(temp)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    if b < a:
        parent[a] = b

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i   

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            if find_parent(parent, i+1) != find_parent(parent, j+1):
                union_parent(parent,i+1,j+1)



check = list(map(int,input().split()))
checklist =set()
for i in check:
    checklist.add(find_parent(parent,i))

if len(checklist) == 1:
    print("YES")
else:
    print("NO")