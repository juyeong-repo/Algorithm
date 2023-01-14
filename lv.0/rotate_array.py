def solution(numbers, direction):
    '''
    source:
    suedo code:
    direction이 left, right인 경우: if문을 사용하여 처리->
        파이썬에서 리스트 원소 순서 변환하는 방법 사용 : list slice (solution1)
        배열 안을 순회하여 순서 변경할 때 : collection lib의 collections.deque 사용 (solutio         n2)
    
    '''
    if direction == 'right':
        return [numbers[-1]] + numbers[:-1]
    else:
        return numbers[1:] + [numbers[0]]
    return answer