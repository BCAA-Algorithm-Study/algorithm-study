n = input()
# n = 'K1KA5CB7'

number = 0
total = ''

for i in n:
    if i.isdigit():
        number += int(i)
    elif i.isalpha():
        total += i
total = sorted(total)
print(''.join(total) + str(number))