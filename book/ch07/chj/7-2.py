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

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(binary_search(array, 4, 0, len(array)-1))