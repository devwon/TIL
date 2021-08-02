# https://programmers.co.kr/learn/courses/30/lessons/82612

# v1
def solution(price, money, count):
    total_price = money - price*count*(count+1)/2
    return -total_price if total_price < 0 else 0

# v2
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)