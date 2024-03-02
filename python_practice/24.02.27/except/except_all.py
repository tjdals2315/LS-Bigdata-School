# 모든 예외 잡기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력: "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외. 발생

except ValueError as exception:
    # ValueError가 발생하는 경우
    print("정수를 입력해 주세요!")
    print(type(exception), exception)

except IndexError as exception:
    # IndexError가 발생하는 경우
    print("리스트의 인덱스를 벗어났어요!")
    print(type(exception), exception)

except Exception as exception: # ValueError와 IndexError가 아닌 예오가 발생했을 때
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception), exception)