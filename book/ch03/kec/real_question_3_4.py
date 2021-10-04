N, K = map(int, input().split())
cnt = 0
while N != 1:
    share, rest = divmod(N, K)
    if share > 0 :
        cnt += rest + 1
        N = share
    else :
        cnt += rest - 1
        break

print(cnt)
