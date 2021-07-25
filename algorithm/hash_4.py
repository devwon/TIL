# https://programmers.co.kr/learn/courses/30/lessons/42579
'''
def solution(genres, plays):    
    from collections import defaultdict
    dd = defaultdict(int)
    for key, val in zip(genres, plays):
        dd[key] += val
    max_order = sorted(dd, reverse=True)

    a = list(zip(genres, plays, list(range(len(genres)))))
    res = sorted(a, key = lambda x: -x[1])
        
    temp, answer = [], []
    #genres에서 2개씩 뽑는 과정
    for i in max_order:
        for j in range(len(res)):
            if res[j][0] == i:
                temp.append(res[j][2])
                if len(temp) == 2:
                    print(temp)
                    answer += temp
                    temp = []
                    break
        # 한개인 경우가 있으므로
        if len(temp) == 1:
            answer += temp
            temp = []
    
    return answer
'''
from collections import defaultdict
def solution(genres, plays):
    answer = [] 
    # { 장르 : 총 재생 횟수 } 사전 
    plays_dict = {}
    # { 장르 : [ ( 플레이 횟수, 고유 번호 ) ] }
    # d = {}
    d = defaultdict(list)
    # 사전들 초기화 
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        plays_dict[genre] = plays_dict.get(genre, 0) + play
        # d[genre] = d.get(genre, []) + [(play, i)]
        d[genre].append((play, i))
    
    # 재생 횟수 내림차순으로 장르별로 정렬 
    sorted_genre = sorted(plays_dict.items(), key=lambda x: -x[1])
    
    # 재생 횟수 내림차순, 인덱스 오름차순 정렬 
    # 장르별로 최대 2개 선택 
    for genre, _ in sorted_genre:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for _, idx in d[genre][:2]]
        
    return answer