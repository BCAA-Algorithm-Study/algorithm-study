N, M = map(int, input().split())
x, y, sight = map(int,input().split())

land = []

for r in range(N) :
    temp = list(map(int, input().split()))
    land.append(temp)
cnt = 1
while True :
    land[x][y] = 1
    if land[x - 1][y] + land[x + 1][y] + land[x][y - 1] + land[x][y + 1] == 4 :
        break
    if sight == 0 :
        sight = 3
        if y == 1 or land[x][y - 1] == 1 :
            continue
        y -= 1
        cnt += 1

    elif sight == 1 :
        sight = 0
        if x == 1 or land[x - 1][y] == 1 :
            continue
        x -= 1
        cnt += 1

    elif sight == 2 :
        sight = 1
        if y == M - 2 or land[x][y + 1] == 1:
            continue
        y += 1
        cnt += 1

    elif sight == 3 :
        sight = 2
        if x == N - 2 or land[x + 1][y] == 1:
            continue
        x += 1
        cnt += 1
    print(x, y)

print(cnt)