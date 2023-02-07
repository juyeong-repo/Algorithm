
'''source:  https://school.programmers.co.kr/learn/courses/30/lessons/120913
1. 정규표현식 사용
2. list comprehension
'''


def solution(my_str, n):
    p = re.compile(f'.{{1,{n}}}')
    return p.findall(my_str)


def solution2(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]