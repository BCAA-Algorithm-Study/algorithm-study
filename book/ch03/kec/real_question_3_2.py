N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))

num_list = sorted(num_list, reverse = True)
answer = 0

while M > 0 :
    if M > K :
        M -= K + 1
        answer += num_list[0] * K
        answer += num_list[1]

    else :
        M = 0
        answer += num_list[0] * M

print(answer)
