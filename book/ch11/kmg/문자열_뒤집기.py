
# s = input()
# s  = "0001100"
s  = "11001100110011000001"

temp = s[0]
_count = {temp: 1, str(int(temp) ^ 1): 0}
for x in s[1:]:
    if temp == x:
        continue
    else:
        temp = x
        _count[x] += 1

print(min(_count.values()))
