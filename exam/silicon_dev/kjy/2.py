import math 
import pandas as pd
import numpy as np

def solution(names, homes, grades):
    answer = []
    homes = list(map(lambda x: math.sqrt(x[0]**2 + x[1]**2), homes))
    grades = list(map(lambda x : math.floor(x), grades))
    df = pd.DataFrame(zip(grades, homes,names), columns = ["grades", "homes", "names"])
    df = df.sort_values(["grades", "homes", 'names'], ascending = (False, False,True))
    index = pd.Series(np.array(1,len(names)+1))
    df = df.set_index(keys=[index], inplace=False, drop=False)
    for name in names:
        answer.append(df[(df['names']==name)].index[0])
    return answer

names = ["azad","andy","louis","will","edward"]
homes = [[3,4],[-1,5],[-4,4],[3,4],[-5,0]]
grades= [4.19, 3.77, 4.41, 3.65, 3.58]
print(solution(names,homes,grades))
