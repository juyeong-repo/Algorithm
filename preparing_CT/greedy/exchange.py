n = 1260
count = 0

array = [500, 100, 50, 10]

# 탐욕적으로 최적의 방안을 찾는 그리디 알고리즘의 결과가 항상 최적의 해를 보장하는지 정당성 검사가 중요하다.

for coin in array:
    # 해당 코인으로 거슬러 줄 수 있는 동전 개수 (나눈 몫)
    count += n //coin 
    n %= coin # 나머지 


print (count)