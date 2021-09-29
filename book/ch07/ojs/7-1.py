import sys

n = int(sys.stdin.readline())
products = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
needs = list(map(int, sys.stdin.readline().split()))

products.sort()
for n in needs:
    s = 0
    f = len(products) - 1
    flag = 0
    while s <= f:
        mid = (s+f)//2
        if products[mid] == n:
            print('yes')
            flag = 1
            break
        elif products[mid] < n :
            s = mid+1
        else:
            f = mid-1
    if flag == 0:
        print('no')