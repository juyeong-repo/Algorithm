from collections import deque


def solution1(numbers, direction):
    '''
    suedo code: 
    1) when direction equals left or right
    2) use python slicing
    이렇게 풀 수 있고 (solution1) 
    파이썬 컬렉션의 deque를 사용해도 된다.  (solution2)
    '''
    if direction == 'right':
        return [numbers[-1]] + numbers[:-1]
    else:
        return numbers[1:] + [numbers[0]]
    return answer


def solution2 (numbers,direction):
    if direction == 'right':
        numbers = deque(numbers)
        numbers.rotate(1)
        return list(numbers)
    else:
        numbers = deque(numbers)
        numbers.rotate(-1)
        return list(numbers)
    