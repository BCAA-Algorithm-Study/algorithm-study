def divide_balance(word):
    balance = 0
    for i in range(len(word)):
        if word[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:     
            return word[:i+1], word[i+1:]

def is_correct(word):
    opening = 0
    close = 0 
    for i in range(len(word)):
        if word[i] == '(':
            opening += 1
        else:
            close +=1
        if opening < close:
            return False
        
    return True

def strip_reverse(word):
    word = word[1:-1]
    temp = ''
    for i in range(len(word)):
        if word[i] == '(':
            temp += ')'
        elif word[i] == ')':
            temp += '('
    return temp

def step(word):
    # print('word: ', type(word))
    if not word:
        return ''

    u, v = divide_balance(word)
    if is_correct(u):
        # print('u: ', u)
        # print('v: ', v)
        # print('step(v): ',type(step(v)))
        u += step(v)
        return u
    else:
        return '(' + step(v) + ')' + strip_reverse(u)
    

def solution(p):
    
    return step(p)

solution("()))((()")