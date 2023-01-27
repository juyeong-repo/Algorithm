#115. 왕실의 나이트

# 현재 나이트의 위치 입력받기
input_data = input() # a1 column->row 순으로 입력받음
row = int(input_data[1]) 
column = int(input_data[0])

# 나이트가 이동할 수 있는 경우의 수
steps = [(-2,-1),(2,-1),(-2,1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = row + step[1]
    
    # 해당위치로 이동 가능하다면 (== 8X8을 벗어나지 않는다면) 카운트 증가
    if 1 <= next_row <= 8 and  1 <= next_column <= 8 :
        result += 1

    print(result)