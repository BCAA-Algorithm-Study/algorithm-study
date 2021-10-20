"""
피보나치 수열 다이나믹 프로그래밍
"""

d = [0] * 100

def fibo_top_down(x): # Dynamic programming Top-down

    if x == 1 or x == 2: # 피보나치 수열의 1, 2번은 1로 고정
        return 1 
    
    if d[x] != 0: # n번째 항을 한번이라도 구하고 저장해놨으면 반환
        return d[x]
    
    d[x] = fibo_top_down(x - 1) + fibo_top_down(x + 2) # n 번째 항을 구하기 위해 필요했던 n-1, n-2 번째항 저장

    return d[x]

def fibo_bottom_up(x): # Dynamic programming Bottom-up
    for i in range(3, x + 1):
        d[i] = d[i -1] + d[i -2]

print(d[99])
