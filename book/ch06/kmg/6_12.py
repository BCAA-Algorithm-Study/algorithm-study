# n, k = map(int, input().split()) # N과 K를 입력 받기
# a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
# b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기
n, k = 5, 3
a = [1,2,5,4,3,]
b = [5,5,6,6,5,]

a.sort()
b.sort(reverse=True)

for i in range(k):
    # swap
    if b[i] > a[i]:
        a[i] = b[i]

print(sum(a))