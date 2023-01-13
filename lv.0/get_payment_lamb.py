def solution(n, k):
    '''
    문제 : 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 
        양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 n과 k가 매개변수로 주어졌을 때, 
        양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.
    출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120830
    suedo code : 
    if n % 10 == 0:  
        answer = (2000 * (k -(n//10)) + (12000 * n)
        return answer
    elif n < 10 and n %1 0 !=0: 
        answer = (12000 * n) + (2000 *  k) 
        return answer 

        -- 파이썬에서는 사칙연산 우선순위 괄호 쓸 필요 없음 !
    '''
    if n>=10 :
        k -= n//10
        return 12000*n + 2000*k
    else:
        return 12000*n + 2000*k
 
def solution2(n,k):
    return 12000 * n + 2000 (k-n//10)