def solution1(spell, dic):
    '''
    source: https://school.programmers.co.kr/learn/courses/30/lessons/120869
    idea: 
    1. 처음 직관적으로 생각한 것은 순회돌기. spell, dic 모두 순회를 돌아 결과값 리턴
    2. sorted(solution1), set(solution2) 사용하는 방법 추가=
    '''
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2


def solution2(spell, dic):
    spell = set(spell)
    for d in dic :
        # https://thecoollife.tistory.com/20 (if not x) 
        if not spell - set(d):
            return 1
    return 2
