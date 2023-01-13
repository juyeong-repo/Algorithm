def solution(s1, s2):
    '''
    resource: https://school.programmers.co.kr/learn/courses/30/lessons/120903
    question: 
    suedo code:
        0. declare 1 variable 'count' initialize w/ '0'
        1. traverse each array
        2. if find s2' char
        3. add 1 number on variable 
        4. return count? 
        
        이게 기본이고 만약 이 문제를 집합 문제라고 생각하면
        1) 교집합 구하기 - solution2
        2) 전체 개수에서 (중복개수 제거안함) - 두개의 합집합 수를 뺀다 - solution3
        https://dojang.io/mod/page/view.php?id=2315 참고 (집합 연산 in python)
        
    '''
    count = 0
    for i in s1:
        if i in s2:
            count +=1
            
    return count

# 합집합은 | 사용
def solution2(s1, s2):
    return len (set(s1) & set(s2))

# 배열끼리 + 하면 합집합이구나 알 수 있음(중복제거됨)
def solution3(s1, s2):
    return len(s1)+ len(s2)- len (set([s1 + s2]))

