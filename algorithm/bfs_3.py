# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

from collections import deque

# v1
def diff_count(str1, str2):
    # 한 번에 한 개의 알파벳만 바꿀 수 있기 때문에 다른 부분 개수 체크
    count = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count += 1
        if count > 1:
            break
    
    return count

def bfs(begin, target, words):
    check = [False for i in range(len(words))]
    answer = 0
    sussess_flag = False
    dq = deque()
    dq.appendleft(begin)

    while len(dq) > 0:
        answer += 1
        for k in range(len(dq)):
            curr_word = dq.pop()
            for i, word in enumerate(words):
                if check[i] == False and diff_count(curr_word, word) == 1:
                    check[i] = True
                    dq.appendleft(word)
                    if word == target:
                        return answer

    return 0


def solution(begin, target, words):
    return bfs(begin, target, words)

# v2
# def solution(begin, target, words):
#     answer = 0
#     Q = [begin]

#     while True:
#         temp_Q = []
#         for word_1 in Q:
#             if word_1 == target:
#                     return answer
#             for i in range(len(words)-1, -1, -1):
#                 word_2 = words[i]
#                 if sum([x!=y for x, y in zip(word_1, word_2)]) == 1:
#                     temp_Q.append(words.pop(i))

#         if not temp_Q:
#             return 0
#         Q = temp_Q
#         answer += 1