import sys
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort(reverse=True)

for i in lst:
    print(i, end=' ')