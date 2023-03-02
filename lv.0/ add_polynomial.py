def solution(polynomial) :
    '''
    Idea:
    다항식에는 일차항과 상수항만 존재한다.
    return 할 때 상수항은 마지막에 둔다.
    항과 연산기호 사이에는 항상 공백 존재
    
    answer = []
    for i in polynomial.split(' '):
        answer.append(i)
    1. 입력값을 polynomial.split(' ')으로 스플릿하여
       -> 선언한 배열에 담는다
    2. 해당 배열을 순회하며
        for j in answer:
            if 'x' in str(i):
            add each element ,,, and if not -> place it
            on last index of array
    -> 근데 이러면 중첩 for문이라 성능면에서 별로일 것 같다
    좀 더 파이써닉하게 해결할 수 있는 방법 분명히 있을텐데
    그게 뭘까 
    
    '''
    return 




def solution2(입력값):
    항 = [0, 0] # x항, 일반항
    for i in 입력값.replace(' ', '').split('+'):
        if 'x' in i:
            if len(i) == 1:
                항[0] += 1
            else:
                항[0] += int(i[:-1])
        else:
            항[1] += int(i)

    # if 항[0] == 1 and 항[1] == 0:
    #     return f"x"
    # if 항[0] == 1 and 항[1] != 0:
    #     return f"x + {항[1]}"
    # 간소화
    if 항[0] == 1:
        return f"x" if 항[1] == 0 else f"x + {항[1]}"

    

    if 항[0] == 0 and 항[1] == 0:
        return f""
    if 항[0] == 0 and 항[1] != 0:
        return f"{항[1]}"
    if 항[0] != 0 and 항[1] == 0:
        return f"{항[0]}x"
    if 항[0] != 0 and 항[1] != 0:
        return f"{항[0]}x + {항[1]}"

