def solution1(n):
    '''
    정수 n을 3x 마을에서 사용하는 숫자로 바꿔 return
    Idea:
    두가지 방법이 있다.
    1. Index(+1해서 나열): [1,2,3,4,5,6,7,8,9,10]
       3x 마을:           [1,2,4,5,7,8,10,11,14,16]
       배열의 인덱스 사용
    2. 배열을 순회하면서 3의 배수 혹은 3이 포함된 숫자는 넘김 
    즉 3의 배수, 3이 들어갈 때는 순회하는 i 값에 1을 더해서 넘긴다
    '''        
    answer = 0
    for _ in range(n): 
        answer += 1
        while '3' in str(answer) or answer % 3 == 0: #3의 배수이거나 3이 들어가는 숫자일경우 1씩 더 추가됨 
            answer += 1
    return answer

# 아니면 제한사항이 1 ≤ n ≤ 100 밖에 없으니까 아래처럼 써도 된다. range는 넉넉히 1000까지로 함
def solution2(n):
    return [i for i in range(1,1001) if i % 3 != 0 and not ('3' in str(i))][n-1]