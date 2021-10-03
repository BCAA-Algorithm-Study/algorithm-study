n = int(input())

array = map(int, input())

m = int(input())

request = map(int, input())

for i in request:
    if i in request:
        print('yes', end = '')
    else:
        print('no', end = '')