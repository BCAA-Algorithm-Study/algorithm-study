#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countSubstrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING input_str as parameter.
#

def countSubstrings(input_str):
    # Write your code here
    print(input_str)
    answer = 0
    length = len(input_str)
    alphabet = ['ab', 'cde', 'fgh','ijk','lmn','opq','rst','uvw','xyz']
    map_alpha_num = dict()
    for idx, alpha in enumerate(alphabet):
        for word in alpha:
            map_alpha_num[word] = idx +1
    alpha_to_num = list(map(lambda x:map_alpha_num[x], input_str))
            

    for i in range(length):
        s = 0
        count =0
        for j in range(i, length):
            s += alpha_to_num[j]
            count +=1
            if s%count == 0:
                answer += 1 

    return answer

if __name__ == '__main__':


# input_str = 'bef'


# answer = 0
# length = len(input_str)
# alphabet = ['ab','cde','fgh','ijk','lmn','opq','rst', 'uvw','xyz']
# map_alpha_num = dict()
# for idx, alpha in enumerate(alphabet):
#     for word in alpha:
#         map_alpha_num[word] = idx+1

# for l in range(1,length+1):
#     start_idx = 0
#     while start_idx + l <= length:
#         temp_word = input_str[start_idx:start_idx+l]
#         s = 0
#         for word in temp_word:
#             s += map_alpha_num[word]
#         if s%l == 0:
#             answer += 1
#         start_idx +=1

# print(answer)