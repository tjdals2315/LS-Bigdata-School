# 반복문으로 팩토리얼 구하기
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))

# 공식과 같은 순서(숫자 순서 반대)
def factorial_reverse(n):
    output = 1
    for j in range(n,0, -1):
        output *= j
    return output
print("1!:", factorial_reverse(1))
print("2!:", factorial_reverse(2))
print("3!:", factorial_reverse(3))
print("4!:", factorial_reverse(4))
print("5!:", factorial_reverse(5))