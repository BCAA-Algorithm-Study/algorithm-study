N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse = True)
for i in range(K) :
    if A[i] < B[i] :
        A[i] = B[i]
    else :
        break
print(sum(A))
