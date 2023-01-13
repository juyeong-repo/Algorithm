def solution(rsp):
    '''
    source: https://school.programmers.co.kr/learn/courses/30/lessons/120839
    question: 가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 re     turn하도록 solution 함수를 완성해보세요.
    
    suedo code:
    1) if문으로 다 처리하면?
    s1 : s2
    2 : 0
    5 : 2
    0 : 5
    s1이 2,5,0 각각의 경우에 0,2,5 를 선언한 문자열 변수에 append한다. 
    ->  제일 직관적이겠지만 다른 방법 없을까
    
    2) 딕셔너리로 정해진 답을 만들어놓고 그걸 호출하도록 하기 -solution2
     파이썬 딕셔너리 정리 : https://github.com/juyeong-repo/python/commit/7086dc93b5db0bf417178fc68f3154cb65484088
    3) 2의 답에 list comprehension 적용 -solution3

    '''
    answer = ''
    for i in rsp:
        if i == '0':
            answer += '5'
        elif i == '2':
            answer += '0'
        elif i == '5':
            answer += '2'
    return answer


def solution2(rsp):
    d = {'0':'5','2':'0','5':'2'}
    answer = ''
    for i in rsp:
        # 이렇게하면 딕셔너리의 key, value에서 해당 key(index)에 해당하는 value 값을 리턴함을 알 수 있음 / https://wikidocs.net/16
        answer += d[i] 
    return answer 


# 리스트 컴프리헨션 https://wikidocs.net/22805 참고
def solution3(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join([d[i] for i in rsp])