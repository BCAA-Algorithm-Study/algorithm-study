"""
문자열 압축
"""
import sys
input = sys.stdin.readline

def compress(s, unit):
    result = ''
    current = 0
    count = 1
    while current < len(s):
        if s[current:current + unit] == s[current+unit : current+2*unit]:
            count += 1
        else:
            if count > 1:
                result += str(count) + s[current:current+unit]
            else:
                result += s[current:current+unit]
            count = 1
        current += unit
    return result


if __name__=="__main__":
    s = input().rstrip()
    mid = len(s) // 2

    min_length = int(1e9)

    for i in range(1, mid + 1):
        compressed = compress(s, i)
        min_length = min(min_length, len(compressed))

    print(min_length)