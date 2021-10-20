# s = input()
s = "02984"
s = "567"

s = map(int, list(s))
mul = 1
for x in s:
    if x == 0:
        continue
    else:
        mul *= x
print(mul)
