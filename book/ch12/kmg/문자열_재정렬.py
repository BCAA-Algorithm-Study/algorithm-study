# s = input()
s = "K1KA5CB7"
string = ""

_int = 0
for x in s:
    if ord(x) <= ord("9"):
        _int += int(x)
    else:
        string += x

print(f"{''.join(sorted(string))}{_int}")
