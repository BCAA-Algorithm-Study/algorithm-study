# input setting
import sys
input = sys.stdin.readline
# n = input()

n = '10100101'

print(min(len(list(filter(lambda x : x != '', n.split('0')))), len(list(filter(lambda x : x != '', n.split('1'))))
))

