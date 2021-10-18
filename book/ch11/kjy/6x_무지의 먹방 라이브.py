from collections import defaultdict
import numpy as np
def solution(food_times, k):
    answer = 0
    dic = defaultdict(int)
    for i in food_times:
        dic[i] += 1
    
    array = sorted(food_times)
    prev = array[0] * dic[array[0]]
    left_length = len(array) - dic[array[0]]

    for i in range(1, len(array)):
        s = (array[i] - array[i-1]) * left_length + prev
        
        if k < s:
            k -= prev
            food_times = np.array(food_times)
            food_times -= array[i-1]
            while k == 0:
                for i in range(len(food_times)):
                    if food_times[i] > 0:
                        food_times[i] -= 1
                        k -= 1
                    if k == 0:
                        return i+1
                        break
            
        left_length -= dic[array[i]]
        prev = s    
 
    return -1