# input setting
import sys
import copy
n = int(input())
array = list(map(int,sys.stdin.readline().rstrip().split()))
calculator = list(map(int,sys.stdin.readline().rstrip().split()))
save = []

def dfs(temp_calculator, number, result):
    if number == n-1:
        # print(number)
        save.append(result)
    for i in range(len(temp_calculator)):
        if temp_calculator[i] > 0: 
            temp = copy.deepcopy(temp_calculator)
            # print(temp)
            temp[i] -= 1
            if i == 0:
                dfs(temp, number+1, result+array[number+1])

            if i == 1:
                dfs(temp, number+1, result-array[number+1])

            
            if i == 2:
                # print(f'temp : {temp}, number : {number} ,result : {result}')
                dfs(temp, number+1, result*array[number+1])

            if i == 3:
                if result < 0 :
                    dfs(temp, number+1, -(-result//array[number+1]))
                else:
                    dfs(temp, number+1, result//array[number+1])

dfs(calculator, 0, array[0])

print(max(save))
print(min(save))
