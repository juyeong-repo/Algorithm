def solution(n):
    '''
    문제 : 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
        제한사항
        0 < n ≤ 1000
    출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120831
    suedo code : 
    짝수 %  2 == 0
    answer = 0
    if  0 < n =< 1000
        answer=+ n
    else:
        continue

        -- 파이썬 range 함수 사용하면 된다. 자바의 switch case 말고 range는 step도 지정 가능 
    '''
    
    return sum (range(0,n+1,2))