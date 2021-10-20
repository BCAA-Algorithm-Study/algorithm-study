"""
문자열 뒤집기
"""
s = input()

zero = 0
one = 0

if s[0] == '0':
    zero += 1
else:
    one += 1

for i in range(len(s)-1):
    if s[i + 1] == s[i]:
        continue
    else:
        if s[i + 1] == '0':
            zero += 1
        else:
            one += 1

print(min(zero, one))