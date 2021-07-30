# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    answer, now, cnt = 0, 0, 0
    current = -1
    task = [] # 작업 대기열
    length = len(jobs)

    while cnt < length:
        # jobs 모든 작업 수행할 때 까지
        for s, t in jobs:
            if current < s <= now:
                # 겹치는 경우 대기열에 넣기
                heapq.heappush(task, [t, s])

        if len(task) != 0:
            # 대기열이 있는 경우
            term, start = heapq.heappop(task)
            current = now
            now += term
            answer += (now - start) # 실제 걸린 시간
            cnt += 1
        else:
            now += 1
    return int(answer / length)