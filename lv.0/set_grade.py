def solution(score):
    sorted_score = sorted([sum(i) for i in score], reverse = True)
    return [sorted_score.index(sum(j))+1 for j in score]