def solution(num_list):
    '''
    문제 : 정수가 담긴 리스트 num_list가 주어질 때, 
    num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
    출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120824
    suedo code : 
    1. num_list 배열을 순회한다.
    2. 짝수는 2로 나눈 나머지가 0.
    3. count 변수를 하나 둔다. 
    4. 짝수인 경우에 count 변수를 증가시킨다.
    5. 홀수는 num_list의 개수에서 짝수 개수를 뺀 것이다.
    6. 짝, 홀수 변수를 튜플에 담는다. 
    '''

    answer = [0,0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        else:
            ansvwer[1] +=1
    return answer


def solution (num_list):
    answer = [0,0]
    for i in num_list:
        answer [i%2] +=1
    return answer

    
