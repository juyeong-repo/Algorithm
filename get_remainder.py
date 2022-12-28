#나머지 구하기 (https://school.programmers.co.kr/learn/courses/30/lessons/120810?language=python3)
# 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

def solution(num1, num2):
    '''
    # suedo code
    1. 사용자로부터 2개의 인자를 입력받는다.
    2. 입력받은 값을 '%' 함수에 태우고 리턴값을 선언한 변수에 저장한다. 
    3. 변수를 출력한다. 
    '''
    answer = num1 % num2
    return answer




# divmod(a, b)
# divmod(10, 3)이라 할때,10을 3으로 나누고 (= 10 / 3) 그 몫인 3과 나머지인 1을 튜플 형식으로 (3, 1)로 반환하는 함수
# 작은수 나눌때는 %같은 사칙연산 함수가 빠르고 큰 수 계산할 때는 divmod가 빠름 

def solution (num1, num2):
     return divmod(num1, num2)[1]