N, M = map(int, input().split())

answer = 0
for row in range(N) :
    temp = list(map(int, input().split()))
    answer = max(answer, min(temp))

print(answer)