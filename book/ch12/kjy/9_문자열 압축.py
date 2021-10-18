# s = input()
s = 'abcabcdede'
if len(s) == 1:
    print(1) # return 1
max_length = len(s) // 2
array = [1001] * (max_length + 1)

for i in range(1, max_length + 1):
    repeat = s[0:i]
    count = 1 
    total = ''
    for j in range(i, len(s), i):
        now = s[j : j+i]
        print(repeat, now)
        if  now == repeat:
            count += 1
        elif now != repeat:
            total += (str(count) + repeat if count != 1 else repeat)
            repeat = now
            count = 1
        
    total += (str(count) + now if count != 1 else now)
    array[i] = len(total)
    print(total)

print(min(array))

