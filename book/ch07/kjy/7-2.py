# n, m = map(int, input().split())

# length = map(int, input().split())

n, m = 4,6
length = [19,15,10,17]

left = 1
right = max(length)
s = 0

while m != s:
    mid = (left + right)//2
    s = sum(list(filter(lambda x : x>0, map(lambda x: x-mid, length))))
    print(s,left,right,mid)
    if m < s:
        left = mid
    elif m > s:
        right = mid
    

print(mid)