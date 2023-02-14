def solution(A, B):
    '''
    source: 
    idea: 
    문자열을 미는 거니까, 처음엔 deque가 문자열을 특정 방향으로 돈다면? 이란 생각을했다.
    그 다음은 인덱스 슬라이싱
    '''
    A = 'hello'
    B = 'ohell'
    str1 = list(A)
    str2 = list(B)
    if str1[1:-1]+str1[0] == str2:
        print ('1')
    print ('-1')