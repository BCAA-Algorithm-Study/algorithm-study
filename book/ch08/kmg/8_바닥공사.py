# x = int(input())
x = 3
# x = 10

d= [1, 3] # x가 1 일경우 1, x가 2일 경우 3

for i in range(2, x):
    d.append(d[1] + (d[0]*2))
    d.pop(0)

print(d[1] % 796796)
