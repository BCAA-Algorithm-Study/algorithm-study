x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

for i in range(2,x+1):
    d[i] = d[i] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
