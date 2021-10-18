string = list(input())
numbers = '0123456789'
number_sum = 0
array = []
for i in string :
    if i in numbers :
        number_sum += int(i)
    else :
        array.append(i)

array.sort()
print(''.join(array) + str(number_sum))
