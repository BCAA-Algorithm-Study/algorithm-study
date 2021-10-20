"""
문자열 재정렬
"""
import sys

input = sys.stdin.readline

S = list(input().rstrip())

alphabet = [x for x in S if ord(x) >= 65 and ord(x) <= 90]
number = [int(x) for x in S if ord(x) >= 48 and ord(x) <= 57]
# print(alphabet, number)
alphabet.sort()

print(''.join(alphabet) + str(sum(number)))