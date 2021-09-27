import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

first = arr[n - 1]
second = arr[n - 2]

mass = m // (k + 1)
res = m % (k + 1)

result = (k * first + second) * mass # One mass is composed of k * first and 1 * second.
result += res * second

print(result)