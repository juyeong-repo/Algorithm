
# 반복적 구현
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례로 곱함
    for i in range(1, n+1):
        result *= i
    return result


# 재귀적 구현 (코드면에서 간결) 
def factorial_recursive(n):
    # n이 1 이하인 경우 1을 반환
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
