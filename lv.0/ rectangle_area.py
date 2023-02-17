def solution(dots): 
    # 인덱스값을 왜 [][]로 지정하지 않아도 되는지 이해 못했음 다시 볼 것
    w = max(dots)[0] - min(dots)[0]
    h = max(dots)[1] - min(dots)[1]
    area = w*h
    return area

def solution(dots):
    # 원래 생각한 방법
    answer = 0
    for i in range(1, len(dots)):
        if dots[i][1] == dots[0][1]:
            width = abs(dots[i][0] - dots[0][0])
        if dots[i][0] == dots[0][0]:
            height = abs(dots[i][1] - dots[0][1])
    answer = width * height
    return answer
