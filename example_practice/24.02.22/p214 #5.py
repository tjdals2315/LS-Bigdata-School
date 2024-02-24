numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(numbers) // 2): # 0, 1, 2, 3
    # j가 1, 3, 5, 7 이 나오려면
    # 어떤 식을 사용해야 할까요?
    j = (i * 2) + 1
    print(f"i = {i}, j = {j}")
    numbers[j] = numbers[j] ** 2
    # 인덱스 번호가 1, 3, 5, 7 인 요소(=> 짝수)를 제곱한다.
print(numbers)

# 실행 결과
# i = 0, j = 1
# i = 1, j = 3
# i = 2, j = 5
# i = 3, j = 7
# [1, 4, 3, 16, 5, 36, 7, 64, 9]