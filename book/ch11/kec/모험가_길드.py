from collections import deque

n = int(input())

team = 0
count = 0

fear = list(map(int, input().split()))
fear.sort()
fear = deque(fear)
max_fear = -1

while fear :
     max_fear = max(fear.popleft(), max_fear)
     count += 1
     if max_fear == count :
         team += 1
         count = 0
         max_fear = -1

print(team)
