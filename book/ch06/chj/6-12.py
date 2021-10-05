""" 두 배열의 원소 교체 """
import sys
readline = sys.stdin.readline

n, k = map(int, input().split())

a = list(map(int , input().split()))
b = list(map(int, input().split()))

a.sort() # 작은 순서대로 정렬
b.sort(reverse=True) # 큰 순서대로 정렬

result = sum(a)
for i in range(k):
    if a[i] >= b[i]: # 더이상 b에서 바꿀 index가 없으면 break
        break
    result += b[i] - a[i]

print(result)