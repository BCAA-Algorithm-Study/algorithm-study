num = int(input())
dasom = int(input())
candidates = [0]        #None 방지
for idx in range(num - 1) :
    vote = int(input())
    if vote >= dasom :
        candidates.append(vote)

cnt = 0
while True :
    candidates = sorted(candidates, reverse = True)
    if dasom <= candidates[0] :
        dasom += 1
        candidates[0] -= 1
        cnt += 1
    else :
        break

print(cnt)
