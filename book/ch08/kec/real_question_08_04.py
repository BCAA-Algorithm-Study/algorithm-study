def floor(n) :
    answer_list  = [0] * n
    answer_list[0] = 1
    answer_list[1] = 3
    for i in range(2, n) :
        answer_list[i] = answer_list[i - 1] + answer_list[i - 2] * 2

    return answer_list[-1]

n = int(input())

print(floor(n) % 796796)
