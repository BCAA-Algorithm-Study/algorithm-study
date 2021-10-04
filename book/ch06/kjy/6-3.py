n, k = map(int, input().split())

a = map(int,input().split())
b = map(int,input().split())

a.sort()
b.sort(reverse = True)

for i in k:
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
