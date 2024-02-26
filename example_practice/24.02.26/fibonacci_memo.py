f_dict = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in f_dict:
        # 딕셔너리에 키가 저장되어있다면 저장(메모)된 값을 리턴
        return f_dict[n]
        # 키가 저장되어 있지 않다면 값을 구함
    # 조기리턴
    output = fibonacci(n - 1) + fibonacci(n - 2)
    f_dict[n] = output # 딕셔너리에 저장
    return output

print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))