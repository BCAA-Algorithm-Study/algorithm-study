number = input()

length = len(number)
total = 0
for i in range(length):
    if i < length // 2 :
        total += int(number[i])
    else:
        total -= int(number[i])

if total == 0:
    print('LUCKY')
else:
    print('READY')
