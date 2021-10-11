def find_price(array, m) :
    answer_list = [10001] * (m + 1)
    answer_list[0] = 0
    for i in range(1, m + 1) :
        for j in array :
            if i - j >= 0 :
                if answer_list[i - j] != -1 :
                    answer_list[i] = min(answer_list[i], answer_list[i - j] + 1)
    if answer_list[-1] == 10001 :
        answer_list[-1] = -1
    return answer_list[-1]

n, m = map(int, input().split())
currency = []
for i in range(n) :
    currency.append(int(input()))

print(find_price(currency, m))
