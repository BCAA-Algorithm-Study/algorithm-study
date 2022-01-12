# input setting
import sys
import copy 
input = sys.stdin.readline
t = int(input())
answers = []


for i in range(t):
    n = int(input())
    answer = []
    def dfs(formula):
        number = formula[-1]
        
        if int(number) == n:
            # print(formula)
            cal = copy.deepcopy(formula).replace(' ','')
            result = eval(cal)
            if result == 0:
                answer.append(formula) 
            return
        
        dfs(formula+' '+str(int(number)+1))
        dfs(formula+'+'+str(int(number)+1))
        dfs(formula+'-'+str(int(number)+1))
    dfs('1')
    answers.append(answer)


for answer in answers:
    answer.sort()
    for formula in answer:
        print(formula)
    print()

        

