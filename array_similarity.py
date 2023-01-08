def solution (s1,s2):
    return len(s1) + len(s2) - len(set([s1+s2]))


def solution (s1,s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
            

