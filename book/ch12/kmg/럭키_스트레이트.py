s = list(int(input()))

# s= '123402'

# s = list(map(int, s))

print("LUCKY" if (sum(s[:len(s)//2]) == sum(s[len(s)//2:])) else "READY")