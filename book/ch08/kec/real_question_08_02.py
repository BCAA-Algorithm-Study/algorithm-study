def make_one(x) :
    answer_list  =[0] * (x + 1)
    i = 1
    while answer_list[x] == 0 :
        i += 1
        answer_list[i] = answer_list[i - 1] + 1
        if i % 2 == 0 :
            answer_list[i] = min(answer_list[i], answer_list[i // 2] + 1)
        if i % 3 == 0 :
            answer_list[i] = min(answer_list[i], answer_list[i // 3] + 1)
        if i % 5 == 0 :
            answer_list[i] = min(answer_list[i], answer_list[i // 5] + 1)

    return answer_list[x]



x = int(input())
print(make_one(x))
