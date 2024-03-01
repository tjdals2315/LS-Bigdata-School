# 콜백함수

def repeat_10(x):
    for i in range(10):
        x()

# 간단한 출력하는 함수
def print_hello(): # print_hello 콜백함수(함수)
    print("안녕하세요")

# 조합하기
repeat_10(print_hello)