# def solution(food_times, k):
#     answer=0
#     food_idx=0
#     t=0
#     l=len(food_times)
#     while t<k:
#         food_idx = food_idx%l
#         cnt = 0
#         while cnt<l and food_times[food_idx] == 0:
#             food_idx = (food_idx+1)%l
#             cnt+=1
#         if cnt==l:
#             return -1
        
#         food_times[food_idx] -= 1
        
#         food_idx+=1
#         t+=1
        
#     food_idx = food_idx%l        
#     cnt = 0
#     while cnt<l and food_times[food_idx] == 0:
#         food_idx = (food_idx+1)%l
#         cnt+=1
#     if cnt==l:
#         return -1
#     else:
#         return food_idx+1