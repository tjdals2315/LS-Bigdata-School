# 재귀 함수로 구현한 피보나치 수열(1)
# 피보나치 수열 = 앞의 두 숫자를 합한 게 다음 숫자 ex. n = 3, f(3) = f(1) + f(2) = 1 + 1 = 2
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

print("1!:", fibonacci(1))
print("2!:", fibonacci(2))
print("3!:", fibonacci(3))
print("4!:", fibonacci(4))
print("5!:", fibonacci(5))

# 같은 계산을 반복하기 때문에 숫자가 커지면 시간이 오래걸리게 된다. -> 메모화 사용