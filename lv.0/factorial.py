from math import factorial
#source: https://school.programmers.co.kr/learn/courses/30/lessons/120848
def solution(n):
    factorial = 1
    i = 1
    while factorial <= n:
        i += 1
        factorial *= i
    return i - 1



def solution2(n):
    i = 1
    while factorial(i) <= n:
        i += 1
    return i - 1