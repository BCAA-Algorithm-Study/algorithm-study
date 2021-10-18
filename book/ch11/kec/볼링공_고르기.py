n, m = map(int, input().split())

balls = list(map(int, input().split()))

count = 0

for a in range(len(balls)) :
    for b in range(a + 1, len(balls)) :
        if balls[a] != balls[b] :
            count += 1

print(count)
