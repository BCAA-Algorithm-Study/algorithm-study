import sys

readline = sys.stdin.readline

def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)    

    else:
        return mid

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

result = []
for target in m_list:
    if binary_search(n_list, target, 0, n-1) != None:
        result.append('yes')
    else:
        result.append('no')

print(' '.join(result))

    