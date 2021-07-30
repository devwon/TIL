# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(s, K):
    heapq.heapify(s)
    cnt = 0
    while s[0] < K:
        if len(s) <= 1:
            return -1
        q = heapq.heappop(s)
        if q < K and len(s) > 0:
            a = heapq.heappop(s)
            heapq.heappush(s, q + a*2)
            cnt += 1
    return cnt