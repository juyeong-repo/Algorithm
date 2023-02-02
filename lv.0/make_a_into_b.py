def solution (before,after):
    ''' 
    source: https://school.programmers.co.kr/learn/courses/30/lessons/120886
    list끼리도 연산자로 비교할 수 있는게 최고네'''

    return 1 if sorted(list(before)) == sorted(list(after)) else 0