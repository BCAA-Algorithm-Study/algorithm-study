# input setting
import sys
import copy
input = sys.stdin.readline

n = int(input())
array = [[] for _ in range(80001)]
answer = []
for i in range(1, n+1):
    q = input().split()
    if q[0] == 'a':
        array[i] = array[i-1] + [int(q[1])]
    elif q[0] == 's' and array[i-1]:
        array[i] = array[i-1][:-1]
    elif q[0] == 't': 
        array[i] = copy.deepcopy(array[int(q[1])-1])
    result = array[i][-1] if array[i] else -1
    answer.append(result)
for i in answer:
    print(i)