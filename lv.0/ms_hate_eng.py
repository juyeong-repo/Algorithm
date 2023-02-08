# source: https://school.programmers.co.kr/learn/courses/30/lessons/120894 
# 딕셔너리 생각했는데 정규표현식으로도 가능할까? -> 딕셔너리+정규표현식으로 풀이 (solution1)
import re

def solution1(numbers):
    s = ''
    d = {'zero':'0',
         'one':'1',
         'two':'2',
         'three':'3',
         'four':'4',
         'five':'5', 
         'six':'6', 
         'seven':'7', 
         'eight':'8',
         'nine':'9'}

        #findall()-정규식과 매칭되는 모든 문자열을 리스트 형식으로 리턴  findall(r'패턴문자열', 문자열) 
    for i in re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine)',numbers):
        s +=d[i]        
    return int(s) 

# 가장 간단한 방법
def solution(numbers):
    return int(numbers.replace('zero','0').replace('one','1').replace('three','3')
               .replace('four', '4').replace('five', '5').replace('six', '6')
               .replace('seven', '7').replace('eight','8').replace('nine', '9')
               )