import sys

readline = sys.stdin.readline

def binary_search(arr, target, start, end):
    
    if start > end:
        return None

    mid = (start + end) // 2
    result = 0
    for i in arr:
        if i > mid:
            result += i - mid
    
    if result == target: # 요청한만큼 자름
        return mid
    
    elif result > target: # 너무 많음 -> 줄이기 위해 start 이동
        return binary_search(arr, target, mid+1, end)
    
    else: # 너무 적음 -> 늘리기위해 end 이동
        return binary_search(arr, target, start, mid-1)

    



n, m = map(int, input().split()) # 떡 개수, 요청 길이

n_list = list(map(int, input().split())) # 떡의 길이

assert len(n_list) == n, "설정한 개수와 입력한 개수가 다름"

print(binary_search(n_list, m, 0, max(n_list)))