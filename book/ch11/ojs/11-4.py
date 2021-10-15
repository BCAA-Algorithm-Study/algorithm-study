import sys

n = int(sys.stdin.readline())
coins = list(map(int,sys.stdin.readline().split()))

coins.sort()


s = {coins[0]}

for i in range(1, len(coins)):
    new_s = set()
    s.add(coins[i])
    for a in s:
        new_s.add(a+coins[i])
    s.update(new_s)

flag = 0
for i in range(1, sum(coins)):
    if i not in s:
        print(i)
        flag = 1
        break

if flag==0:
    print(sum(coins)+1)