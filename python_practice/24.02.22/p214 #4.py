numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number + 2) % 3 ].append(number)
    #[]안에 인덱싱이 들어가야 함
print(output)

# 실행 결과 [[1, 4, 7], [2, 5, 8], [3, 6, 9]]