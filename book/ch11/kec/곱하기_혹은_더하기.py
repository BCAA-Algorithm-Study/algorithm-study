numbers = list(input())
result = 0

for n in numbers :
    result = max(result + int(n), result * int(n))

print(result)
