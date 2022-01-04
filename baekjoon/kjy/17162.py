# input setting
import sys
from collections import deque
input = sys.stdin.readline
q, mod = map(int,input().split())
mod_array = [[] for _ in range(mod)]
array = []
order = 0
answer = []
for i in range(q):
    n = list(map(int,input().split()))
    
    if n[0] == 1:
        remain = n[1]%mod
        mod_array[remain].append(order)
        array.append(remain)
        order += 1        
          
    elif n[0] == 2 and array:
        remain = array.pop()
        mod_array[remain].pop()
        order -= 1

    elif n[0] == 3:
        if all(mod_array):
            maximum_array = [idx_array[-1] for idx_array in mod_array]
            answer.append(max(maximum_array) - min(maximum_array) + 1)
        else:
            answer.append(-1)
    # print(f'mod_array /: {mod_array}, order: {order}')

for i in answer:
    print(i)