def food_storage(array, n) :
    answer_list = [0] * (n + 1)
    answer_list[1] = array[0]
    for i in range(2, n + 1) :
        answer_list[i] = max(answer_list[i - 1], answer_list[i - 2] + array[i - 1])

    return answer_list[-1]
n = int(input())
storage = list(map(int, input().split()))

print(food_storage(storage, n))
