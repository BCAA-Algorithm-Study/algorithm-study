# x = int(input()))
x = 26

d = [0, 0]

for x in range(2, x+1):
    d.append(d[x-1]+1)

    if x % 2 == 0:
        d[x] = min(d[x], d[x//2]+1)
    if x % 3 == 0:
        d[x] = min(d[x], d[x//3]+1)
    if x % 5 == 0:
        d[x] = min(d[x], d[x//5]+1)

print(d[x])