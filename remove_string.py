import re

def solution (my_string, letter):
    '''
    question :
    문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

    제한사항
    1 ≤ my_string의 길이 ≤ 100
    letter은 길이가 1인 영문자입니다.
    my_string과 letter은 알파벳 대소문자로 이루어져 있습니다.
    대문자와 소문자를 구분합니다.

    resource: https://school.programmers.co.kr/learn/courses/30/lessons/120826
    suedo code :
    for나 if 문 사용? x python replace 함수 사용하기. 
    but 문자열은 뒤로갈수록 어려워지기 때문에 정규표현식 이용한 방법도 사용해보기
    
    정규표현식은 특정 문자열 패턴을 찾아서 바꾸거나 제거해준다.
    
    
    '''
    return re.sub(letter, '', my_string)


# replace 함수사용 
def solution2(my_string, letter):
    return my_string.replace (letter, '')