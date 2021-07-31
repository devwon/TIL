# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3
# v1은 온전히 나의 힘으로 푼 코드!!

import heapq
import re

def solution(operations):
    tasks = []
    q = []
    for i in range(len(operations)):
        heapq.heappush(tasks, [i, operations[i]])

    while len(tasks) > 0:
        # v1
#         operation = heapq.heappop(tasks)[1]

#         if operation.startswith('I'):
#             # 숫자 삽입
#             heapq.heappush(q, int(''.join(map(str, re.findall('[+-]?\d+', operation)))))
#         elif operation == 'D 1' and len(q) > 0:
#             # 최대값 삭제
#             q = heapq.nlargest(len(q), q)[1:]
#             heapq.heapify(q)
#         elif operation == 'D -1' and len(q) > 0:
#             # 최솟값 삭제
#             heapq.heappop(q)
        
        # v2
        operation = heapq.heappop(tasks)[1]
        command = operation[0]
        value = int(operation[2:])
        if command == 'I':
            # 숫자 삽입
            heapq.heappush(q, int(''.join(map(str, re.findall('[+-]?\d+', operation)))))
        elif len(q) != 0:
            if value > 0:
                # 최대값 삭제
                q = heapq.nlargest(len(q), q)[1:]
                heapq.heapify(q)
            else:
                # 최솟값 삭제
                heapq.heappop(q)
    answer = [heapq.nlargest(1, q)[0], q[0]] if len(q) > 0 else [0, 0]
    
    return answer