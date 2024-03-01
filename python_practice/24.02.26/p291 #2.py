# 입력한 모든 값을 곱하는 함수

def mul(*values):
    output = 1 # 함수에서 선언할 초깃값이 중요함!
    for value in values:
        output += value
    return output

# 함수를 호출합니다.
print(mul(5, 7, 9, 10))