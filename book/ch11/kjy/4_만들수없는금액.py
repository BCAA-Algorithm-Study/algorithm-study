# input setting
import sys
input = sys.stdin.readline
# n = int(input())
# array = []
# for i in range(n):
#     array.append(int(input()))
n=5
array = [3,2,1,1,9]
array.sort(reverse = True)
INF = int(1e6)
gg = 0
# 최소 단위 1부터 반복
for i in range(1, INF):
    # 큰 단위 화폐로부터 0이 나올 때까지 빼기 
    sub = i
    for j in range(len(array)):
        sub -= array[j]
        print(sub,i, array[j])
        if sub < 0:
            sub += array[j]
        elif sub == 0:
            break
        elif j == n-1:
            print(i)
            gg = 1
    if gg:
        break


'''
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

'''