def solution1(str1, str2):

    '''
    source: https://school.programmers.co.kr/learn/courses/30/lessons/120908
    solution1 수정해야함 
    '''

    str1 = "ab6CDE443fgh22iJKlmn1o"	
    str2 = "6CD"
    if (sorted(set(str1)) - sorted(set(str2))) == len(str1):
        return 2
    return 1





def solution2(str1, str2):
    if str2 in str1:
        return 1
    return 2