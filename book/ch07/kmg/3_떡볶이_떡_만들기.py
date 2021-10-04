import sys

# n, m, nl = sys.stdin.readlines().strip()
n, m, nl = 4, 6, [19, 15, 10, 17]

end = max(nl)
start = 0

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for x in nl:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid -1
    else:
        print(mid)
        result = mid
        start = mid +1
    
print(result)