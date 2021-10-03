n = int(input())

number = []
for i in range(n):
    number.append(int(input()))

for i in sorted(number, reverse=True):
    print(i, end = '')

