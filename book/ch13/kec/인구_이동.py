# https://www.acmicpc.net/problem/16234
import pprint

def make_union(world_map, l, r) :
    temp_map = [list(range(n * i + 1, n * (i + 1) + 1)) for i in range(n)]
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in range(n) :
        for j in range(n) :
            for dx, dy in move :
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < n :
                    if l <= abs(world_map[i][j] - world_map[x][y]) <= r :
                        temp_map[i][j] = min(temp_map[i][j], temp_map[x][y])
                        temp_map[x][y] = min(temp_map[i][j], temp_map[x][y])
    return temp_map

def union(world_map, union_map) :
    union_dict = {}
    sum_dict = {}
    for i in range(n) :
        for j in range(n) :
            if union_map[i][j] not in union_dict.keys() :
                union_dict[union_map[i][j]] = [(i, j)]
                sum_dict[union_map[i][j]] = world_map[i][j]
            else :
                union_dict[union_map[i][j]].append((i, j))
                sum_dict[union_map[i][j]] += world_map[i][j]
    
    for k, v in union_dict.items() :
        length = len(v)
        aver = sum_dict[k] // length
        for r, c in v :
            world_map[r][c] = aver

n, l, r = map(int, input().split())
world_map = []

for i in range(n) :
    temp = list(map(int, input().split()))
    world_map.append(temp)

cnt = 0
while True :
    union_map = make_union(world_map, l, r)
    valid_map = [list(range(n * i + 1, n * (i + 1) + 1)) for i in range(n)]
    if valid_map == union_map :
        break
    union(world_map, union_map)
    pprint.pprint(union_map, width = 20)
    pprint.pprint(world_map, width = 30)
    cnt += 1

print(cnt)