def binary_search(min_length, max_length, array, target) :
    mid = (min_length + max_length) // 2
    temp = sum([i - mid for i in array if i > mid])
    if temp == target :
        return mid
    elif temp > target :
        return binary_search(mid, max_length, array, target)
    elif temp < target :
        return binary_search(min_length, mid, array, target)



n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))
rice_cakes.sort()

print(binary_search(rice_cakes[0], rice_cakes[-1], rice_cakes, m))
