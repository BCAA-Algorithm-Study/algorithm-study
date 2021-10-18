n = int(input())
coins = list(map(int, input().split()))
coins.sort()

price = 1
for i in coins :
    if price < i :
        break
    price += i

print(price)
