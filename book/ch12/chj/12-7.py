"""
치킨 배달
"""
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

houses =[]
chickens = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            houses.append([i, j])
        elif line[j] == 2:
            chickens.append([i, j])

def get_distance(houses, chickens):
    chicken_distance = 0
    for hx, hy in houses:
        min_distance = int(1e9)
        for cx, cy in chickens:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)

        chicken_distance += min_distance

    return chicken_distance

comb_chickens = list(combinations(chickens, m))

chicken_distance = int(1e9)

for chicken in comb_chickens:
    chicken_distance = min(chicken_distance, get_distance(houses, chicken))

print(chicken_distance)

