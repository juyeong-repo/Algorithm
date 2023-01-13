def solution(array, height):
    
    '''
    문제 : 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 
    머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 
    머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.
        1 ≤ array의 길이 ≤ 100
        1 ≤ height ≤ 200
        1 ≤ array의 원소 ≤ 200


    츌처 : https://school.programmers.co.kr/learn/courses/30/lessons/120585
    suedo code :
    use sort function .. bubble sort? 정렬의 종류들 중에 가장 효율적인 것을 적용
    sort.array
    array 순서를 뱉는 함수가 있을 것 
    and if height < array
    than total count of array minus ..
    
    '''
    count = 0
    for i in array :
        if i > height :
            count += 1
    return count

def solution2 (array, height):
    array.append(height)
    return sorted(array, reverse = True).index(height)

def solution3 (array, height):
    '''
    filter함수는 두번째 인자로 넘어온 데이터(array)중에서 첫번째 인자로 넘어온 조건 함수를 만족하는
    데이터만을 반환한다. (출처: daleseo.com/python-filter/)
    '''
    return len(list(filter(lamda x:x > height, array)))

    