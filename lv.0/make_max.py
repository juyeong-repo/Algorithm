#source: 
def solution(numbers):
    answer = sorted(numbers, reverse = True)
    return answer[0] * answer[1]


def solution1(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]

