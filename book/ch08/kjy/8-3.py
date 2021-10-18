# n = int(input())
n=3

if n % 2 == 0:
    answer = 3 ** (n//2) - 1
else:
    answer = (n//2 + 1) * 3 ** (n//2) - 1 

print(answer % 796796)