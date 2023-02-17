def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer



def solution2(strlist):
    return [len(str) for str in strlist]