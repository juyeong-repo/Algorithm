from collections import counter 

def solution(array, n):
    '''
    문제 : 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, 
    array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
    출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120583
    suedo code : 

    def solution(array, n):
    return len(list(filter(lamda x:x = n , array))) // 요거 에러

    '''
    count = 0
    for i in array:
        if i == n:
            count += 1 
    return count


# 가장 간단한 방법
def solution2 (array, n):
    array.count(n)


# if 배열이 [1,1,2,3,4,11] 로 주어지고, 1의 갯수를 구하라고 하면 
def solution3 (array, n):
    str(array).count(n)


'''
 Collections의 counter 사용
 counter 생성자는 여러 형태의 데이터 형태를 인자로 받는다. 중복된 데이터가 저장된 배열을 인자로 넘기면 
 각 원소가 몇번씩 나오는지 저장된 객체를 얻는다. 
 : https://www.daleseo.com/python-collections-counter/
    https://www.youtube.com/watch?v=0EQlGF-ITi8
'''

# from collections import counter 
def solution4 (array, n):
    return Counter(array).get(n)
    
 