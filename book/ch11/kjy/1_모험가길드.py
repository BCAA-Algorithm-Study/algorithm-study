# input setting
# import sys
# input = sys.stdin.readline
# n = int(input())

# array = list(map(int,input().split()))
n=5
array = [2, 3, 1, 2, 2]
count = 0
count_people = 0
idx = 1 
# 공포도가 가장 높은 사람 기준 정렬하기
array.sort(reverse = True)
array = [0] + array
print(array)
for i in range(1, n):
    # 가장 높은 공포도의 수 이상만큼 인덱스 업데이트
    count_people += 1
    print(idx, count_people)
    if array[idx] >= count_people:
        idx = i
        # 그룹을 뽑고 가장 높은 공포도와 남은 인원의 수 비교
        if array[i+1] <= n-i:
            count+=1
            count_people -= array[idx]
print(count)
