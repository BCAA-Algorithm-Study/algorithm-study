n = int(input())
array = set(map(int, input().split()))
# print(array)

m = int(input())
x = list(map(int, input().split()))

for i in x :
    if i in array :
        print('yes', end = ' ')
    else :
        print('no', end = ' ')
