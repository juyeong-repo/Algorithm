
def solution1(emergency):
    sorted_emergency = sorted(emergency, reverse = True)
    return [sorted_emergency.index(i) + 1 for i in emergency]


def solution2(emergency):
    sorted_emergency = sorted(emergency, reverse = True)
    return list(map(lambda x: sorted_emergency.index(x) + 1, emergency))

'''
source: https://school.programmers.co.kr/learn/courses/30/lessons/120835
idea: list comprehension , lambda
'''