n= int(input())

L= list()
for _ in range(n):
    L.append(int(input()))

L.sort(reverse=True)
print(*L)