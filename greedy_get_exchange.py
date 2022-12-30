# Using Greedy Algorithm to get monney exchange.


n= 1260
count = 0

# 큰 단위 화폐부터 차례로 확인
coin_types = [500, 100, 50, 10]

# suedo code 
# 500 카운트

for coin in coin_types:
    count += n #해당화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)

