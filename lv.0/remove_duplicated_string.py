def solution(my_string):
    '''
    source: https://school.programmers.co.kr/learn/courses/30/lessons/120888
    idea: 
    - 중복된 문자를 제거한다 -> set
    - 순서를 지키면서 합칠 수 있는 것 -> 딕셔너리 사용
        여기서는 dict.fromkeys(순회할 자료, 키에 매핑될 값) 사용 
        -> 키에 매핑될 값은 생략 가능함
    '''
    return ''.join(dict.fromkeys(my_string))