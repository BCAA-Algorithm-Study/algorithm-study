from collections import deque

def segment(x, space):
    # Write your code here
    # print(x,space)
    
    n = len(space)
    deq = deque()
    res = []
    i = 0
    while i < n:
        if deq and deq[0] == i-x:
            deq.popleft()
        while deq and space[deq[-1]] > space[i]:
            deq.pop()
        deq.append(i)
        
        if i >= x - 1:
            res.append(space[deq[0]])
        i+=1
    return max(res)

    #https://stackoverflow.com/questions/66079780/time-and-space-complexity-of-the-max-disk-space

# length = len(space)
# dp = [0]*length
# temp = deque(space[:x])
# dp[0] = min(temp)
# min_idx = temp.index(dp[0])
# prev_i = 0

# for i in range(1, length-x+1):
#     if i <= min_idx:
#         dp[i] = min(dp[i-1],space[i+x-1])
#         if dp[i]!=dp[i-1]:
#             min_idx = i+x-1
#     else:
#         temp = space[i:i+x]
#         dp[i] = min(temp)
#         min_idx = i + temp.index(dp[i])
#         prev_i = i
#         print('dp',dp[i],i,min_idx)
    
# return max(dp)