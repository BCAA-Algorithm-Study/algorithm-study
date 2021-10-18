import sys
s = list(sys.stdin.readline().strip())
num = 0
result = []
for i in s:
    if i.isdigit():
        num += int(i)
    else:
        result.append(i)

result.sort()
result = ''.join(result)
print(result+str(num))