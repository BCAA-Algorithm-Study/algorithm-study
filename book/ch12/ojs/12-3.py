def solution(s):
    min_length = len(s)
    for i in range(1, len(s)//2+1):
        cnt = 1
        new_s = ''
        j=0
        while j<len(s):
            # print(s[j:j+i], s[j+i: j+i+i])
            if s[j:j+i] == s[j+i: j+i+i]:
                cnt+=1
                j+=i
            else:
                if cnt==1:
                    new_s += s[j:j+i]
                    j+=i
                else:
                    new_s += str(cnt) + s[j:j+i]
                    j+=i
                    cnt=1
        # print(new_s , len(new_s))
        min_length = min(min_length, len(new_s))
    return min_length