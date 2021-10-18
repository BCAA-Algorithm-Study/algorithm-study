# n = int(input())
# coins = map(int, input())
# 

n, coins = 5, [3,1,1,9]

temp =1 
for x in sorted(coins):
    print(temp ,x )
    if temp < x:
        break
    else:
        temp += x

print(temp)

