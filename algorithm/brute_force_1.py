# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    scores = [0,0,0]
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    l = len(answers)
    res = []
    
    # 점수 채점
    for i in range(l):
        if answers[i] == p1[i%5]:
            scores[0] += 1
        if answers[i] == p2[i%8]:
            scores[1] += 1
        if answers[i] == p3[i%10]:
            scores[2] += 1
    # 결과값 정제
    '''
    for p, s in enumerate(scores):
        if s == max(scores):
            res.append(p+1)
    return res
    '''
    return [i + 1 for i, v in enumerate(scores) if v == max(scores)]