columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

c, r = list(input())
r = int(r)
c = columns.index(c.lower()) + 1

u = min(r - 1, 2)
d = min(8 - r, 2)
l = min(c - 1, 2)
r = min(8 - c, 2)

move = ((u + d) * (l + r)) / 2
print(int(move))