# https://programmers.co.kr/learn/courses/30/lessons/60058
def solution(p):
    if not p : return p
    balance = 0

    # 올바른 문자열인지 확인
    def check_collect(p) :
        open = 0
        close = 0
        for i in range(len(p)) :
            if p[i] == '(' : open += 1
            else : close += 1
            if open - close < 0 :
                return False
        return True

    # 올바른 문자열이면 p 반환
    if check_collect(p) :
        return p

    # 올바른 문자열이 아닐 때,
    # u, v 나누기
    for i in range(len(p)) :
        if p[i] == '(' : balance += 1
        else : balance -= 1
        if balance == 0 :
            u = p[ : i + 1]
            v = p[i + 1 : ]
            break

    # follow manual
    if check_collect(u) :
        answer = u + solution(v)

    else :
        answer = '(' + solution(v) + ')'
        u = ''.join(list(map(lambda x :  '(' if x == ')' else ')', u[1 : -1])))
        answer += u

    return solution(answer)

solution("()))((()")
