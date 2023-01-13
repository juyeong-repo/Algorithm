import math

def solution(n):
    '''
    문제 :머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 
    모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
    출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120814
    suedo code: 
        한판 = 7조각
        전체 인원수 n / 7 .. 나머지가 있다면, 올림처리 해야함.
            if n // 7 == 0: --나머지
                return n // 7
            else:
                return n // 7 + 1

            -- 이건 너무 자바식 풀이같다.
            파이썬의 올림함수 사용하면 ..

            import math
            math.ceil (n/7) 

    '''

    if n // 7 = n / 7:
        return n // 7
    else:
        return n // 7 +1


def solution2 (n):
    return math.ceil(n/7)
    
