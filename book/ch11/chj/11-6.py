"""
무지의 먹방 라이브
https://programmers.co.kr/learn/courses/30/lessons/42891
"""
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

k = int(input())
food_times = list(map(int, input().split()))

def solution(k, food_times):
    if sum(food_times) < k:
        return -1

    

    return None