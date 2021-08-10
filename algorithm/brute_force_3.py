# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    # v1
    s = brown + yellow
    for w in range(s, 2, -1):
        # w: width, h: height
        if s % w == 0:
            h = s // w
            if yellow == (w-2)*(h-2):
                return [w, h]
    #v2
    '''
    ans=((brown-4)+math.sqrt((brown-4)**2-16*yellow))//4
    return [ans+2,yellow//ans+2]
    '''