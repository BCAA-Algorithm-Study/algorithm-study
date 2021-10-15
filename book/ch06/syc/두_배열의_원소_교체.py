n,k = map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

print('A is:',A)
print('B is:',B)

A[:k],B[:k] = B[:k],A[:k]

print('new A is:',A)
print('new B is:',B)

print(sum(A))