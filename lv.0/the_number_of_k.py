def solution(i, j, k):
    '''
    source: https://school.programmers.co.kr/learn/courses/30/lessons/120887
    idea: 전체를 문자열로 변환해주면 된다. 
    '''
    return str(list(range(i, j+1))).count(str(k))


def solution2(i, j, k):
    # list의 sum 사용
    answer = sum([str(i).count(str(k)) for i in range(i,j+1)])
    return answer