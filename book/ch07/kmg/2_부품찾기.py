import sys

# n, nl, m, ml = sys.stdin.readlines().rstip()
n, nl, m, ml = 5, [8,3,7,9,2], 3, [5,7,9]

# U(understand): 중복에 대해서 어떻게 처리?
# M(match): find를 사용해서 구현예정
# P(plan): ml에서 하나씩 빼서 nl로 찾을 예정

answer = []
for _index in ml:
    try: 
        nl.index(_index)
        answer.append("yes")
    except:
        answer.append("no")

print(" ".join(answer))


# R(review): O(n), 하용한 함수 index,  append는 O(1)의 시간복잡도를 가지고, 반복문으로 전체를 확인 하니깐, 
# E(evalute): ..
