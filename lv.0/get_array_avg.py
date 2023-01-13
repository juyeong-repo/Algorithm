import numpy as np

def solution(numbers):
    '''
    문제 :정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

    제한사항
    0 ≤ numbers의 원소 ≤ 1,000
    1 ≤ numbers의 길이 ≤ 100
    정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다.

    출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120817
    suedo code : 평균 == total //  n
     -- 배열로 입출력 들어오는데, 입출력 체크하고 문제 풀기. 
     
     이 때 입력의 특정행,열의 합을 구하고 싶다면, 파이썬의 numpy sum 개념 사용 (solution2)
     평균을 구하고 싶다면 np.mean(numbers) 
    '''
    
    return sum(numbers) / len(numbers)



def solution2(numbers):
    return np.sum(numbers)/len(numbers)

def solution3(numbers):
    return np.mean(numbers)
    
