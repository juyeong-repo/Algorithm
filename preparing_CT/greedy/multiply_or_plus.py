data = input ()

# 첫 번째 문자를 숫자로 변경하여 대입 
result = int(data[0])

# 두 번째 문자부터 더하기 혹은 곱하기 수행 
for i in range (1,len(data)) :
    # 두 수중 하나라도 '0' 혹은 '1'인 경우, 곱하기말고 더하기 수행
    if num <=1 or result <=1:
        result += num
    else:
        result *= num

print (result)