# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    length = len(s)
    best_length = length
    if length == 1:
        return 1
    for i in range(1, length // 2 + 1) :
        string = ''
        cnt = 1
        temp = s[:i]
        for j in range(i, length, i) :
            if temp == s[j:j + i] :
                cnt += 1
            else :
                if cnt == 1 :
                    cnt = ''
                string += str(cnt) + temp
                cnt = 1
                temp = s[j : j + i]
        else :
            if cnt == 1 :
                cnt = ''
            string += str(cnt) + temp
        best_length = min(best_length, len(string))

    return best_length
