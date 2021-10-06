n= int(input())

L=list()
for _ in range(n):
    name, score = input().split()
    score = int(score)

    L.append((name,score))

    L.sort(key = lambda x : x[1])
    
ans=list()
for i in L:
    ans.append(i[0])
    
print(*ans)