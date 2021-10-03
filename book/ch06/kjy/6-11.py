n = int(input())

array = []
for i in range(n):
    input = input().split()
    array.append(input[1],int(input[0]))

for score, name in sorted(array):
    print(name, end = '')
    

