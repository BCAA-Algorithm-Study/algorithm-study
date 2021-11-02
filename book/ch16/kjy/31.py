# input setting
import sys
import copy
t = int(input())
answer = []
for i in range(t):
    n, m = map(int,sys.stdin.readline().rstrip().split())

    array = []
    index_array = [[0,0]]
    total = 0
    temp = list(map(int,sys.stdin.readline().rstrip().split()))

    for i in range(0,len(temp),m):
        array.append(temp[i:i+m])
        if array[i//m][0] > total:
            index_array.pop()
            index_array.append([i//m,0])
            total = array[i//m][0]
 
    dp = []
    temp2 = 0
    for j in range(1,m):
        prev_i, prev_j = index_array.pop()
        if prev_i == 0:
            for i in range(prev_i, prev_i+2):
                if temp2 < total + array[i][j]:
                    index_array.append([i,j])
                    temp2 = total + array[i][j]
        elif prev_i == n-1:
            for i in range(prev_i-1,prev_i+1):
                if temp2 < total + array[i][j]:
                    index_array.append([i,j])
                    temp2 = total + array[i][j]
        else:
            for i in range(prev_i-1,prev_i+2):
                if temp2 < total + array[i][j]:
                    index_array.append([i,j])
                    temp2 = total + array[i][j]
  
        total = temp2
        dp.append(total)

    answer.append(max(dp))
for i in answer:
    print(i)





