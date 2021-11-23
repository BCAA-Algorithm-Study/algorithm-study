# input setting
import sys
from collections import defaultdict
import copy


input = sys.stdin.readline
answer = []
n = int(input())

for _ in range(n):
    t = int(input())
    last_rank = list(map(int,input().split()))
    team_dict = defaultdict(int)
    for rank, team_num in enumerate(last_rank):
        team_dict[team_num] = rank
    m = int(input())
    temp_dict = copy.deepcopy(team_dict)
    for _ in range(m):
        a,b = map(int,input().split())
        if team_dict[a] > team_dict[b]:
            temp_dict[a] -= 1
            temp_dict[b] +=1
        else:
            temp_dict[a] += 1
            temp_dict[b] -=1
    
    if len(set(temp_dict.values())) != t:
        answer.append("IMPOSSIBLE")
    else:
        realign = sorted(temp_dict.items(),key=lambda x:x[1])
        realign = list(map(lambda x:x[0], realign))
        answer.append(realign)

for i in answer:
    if i == 'IMPOSSIBLE':
        print(i)
    else:
        print(*i)
# 기존에 존재하던 순위는 유지
# 순서쌍에 해당하면 바뀌어야 함


