#!/bin/python3

# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    # v1
    '''
    if all(n == 0 for n in numbers):
        return '0'

    numbers = list(map(str, numbers))
    return ''.join(sorted(numbers, key = lambda n: n*3, reverse=True))
    '''
    
    # v2
    numbers = ''.join(sorted(map(str, numbers), key = lambda n: n*3, reverse=True))
    return str(int(numbers))