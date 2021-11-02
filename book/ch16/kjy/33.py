n = int(input())
t = []
p = []
for i in range(n):
    T, P = map(int,input().split())
    t.append(T)
    p.append(P)
# t=[3, 5, 1, 1, 2, 4, 2]
# p=[10, 20, 10, 20, 15, 40, 200]

dp = [0] * (n+1)
# print(t)
# print(p)
for i in range(n):
    if t[i]+i < n+1 : 
        # print(f'dp : {dp},dp[t[i]+i] : {dp[t[i]+i]},dp[i] + p[i] : {dp[i] + p[i]}, i {i}, p[i] : { p[i]}, t[i] : {t[i]}')
        dp[t[i]+i] = max(dp[t[i]+i], dp[i] + p[i])
        for j in range(t[i]+i, n+1):
            # print(j, t[i]+i)
            if dp[j] < dp[t[i]+i]:
                dp[j] = dp[t[i]+i] 

print(max(dp))

