# 이진탐색

```
nums = [0,1,2,3,4,5,6,7,8,9] 
n = 5 l = 0 
r = len(nums)-1 
result = 0 
while l <= r: 
    mid = (l+r) // 2 
    if nums[mid] >= n: 
    result = mid 
    r = mid - 1 
    else: 
    l = mid + 1 
    print(result) 
    
    ''' 
    결과값 5
    ```
```
[출처](https://programming119.tistory.com/196)

## 예제 1
```
from bisect import bisect_left, bisect_right 
nums = [0,1,2,3,4,5,6,7,8,9] 

n = 5 

print(bisect_left(nums, n)) 
print(bisect_right(nums, n)) 
''' 결과값 5 6 '''
```

## 예제 2
```
from bisect import bisect_left, bisect_right 
nums = [4, 5, 5, 5, 5, 5, 5, 5, 5, 6] 

n = 5 

print(bisect_left(nums, n)) 
print(bisect_right(nums, n)) 
''' 결과값 1 9 '''
```
