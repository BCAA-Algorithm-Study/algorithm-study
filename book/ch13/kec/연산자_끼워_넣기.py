# https://www.acmicpc.net/problem/14888

import copy

n = int(input())
numbers = list(map(int, input().split()))
operater = list(map(int, input().split()))
answer = []
result = numbers.pop(0)

def dfs(numbers, operater, result, cals) :
    num_cpy =copy.deepcopy(numbers)

    if cals == n - 1 :
        # print(result)
        answer.append(result)
    else :
        k = num_cpy[cals]

        if operater[0] :
            # print(result, '+', k)
            temp = result + k
            op_temp = copy.deepcopy(operater)
            op_temp[0] -= 1
            dfs(numbers, op_temp, temp, cals + 1)

        if operater[1] :
            # print(result, '-', k)
            temp = result - k
            op_temp = copy.deepcopy(operater)
            op_temp[1] -= 1
            dfs(numbers, op_temp, temp, cals + 1)

        if operater[2] :
            # print(result, '*', k)
            temp = result * k
            op_temp = copy.deepcopy(operater)
            op_temp[2] -= 1
            dfs(numbers, op_temp, temp, cals + 1)

        if operater[3] :
            # print(result, '/', k)
            if result > 0 :
                temp = result // k
            else :
                temp = -(-result // k)
            op_temp = copy.deepcopy(operater)
            op_temp[3] -= 1
            dfs(numbers, op_temp, temp, cals + 1)


dfs(numbers, operater, result, 0)

print(max(answer))
print(min(answer))
