# https://www.acmicpc.net/problem/18406
score = list(map(int, list(input())))
score_head = sum(score[:(len(score) // 2)])
score_tail = sum(score[(len(score) // 2):])

if score_head == score_tail :
    print('LUCKY')
else :
    print('READY')
