import re

def solution1(order):
    '''
    source:
    idea:
    1. count() 를 이용하여 풀기 (solution1)
    2. lambda() 사용 (solution2)
    3. filter() 사용 (solution3)
    4. 정규표현식의 findall() 사용 (solution4)
    '''
    answer = 0
    order = str(order)
    answer += order.count('3')
    answer += order.count('6')
    answer += order.count('9')
    return answer


def solution2(order):
    order = str(order)
    return sum(map((lambda x: order.count(x), '369')))


def solution3(order):
    order = str(order)
    return len(list(filter(lambda x: x in '369', order))) 


def solution4(order):
    order = str(order)
    return len(re.findall('[369]', order))