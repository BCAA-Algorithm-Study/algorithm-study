def binary_search(start, end, array, target) :
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return 'yes', mid
        elif array[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    return 'no', mid

def check_order(array, customer_list) :
    start = 0
    end = N - 1
    answer_list = []
    for order in customer_list :
        answer, start = binary_search(start, end, store_list, order)
        answer_list.append(answer)
    return answer_list

N = int(input())
store_list = list(map(int, input().split()))
store_list.sort()
M = int(input())
customer_list = list(map(int, input().split()))
customer_list.sort()

(' ').join(check_order(store_list, customer_list))
