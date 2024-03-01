# p214 문제 3

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0:
        print(number, "는 짝수입니다.")
    else:
        print(number, "는 홀수입니다.")

for number in numbers:
    print(number, "는", len(str(number)), "자릿수입니다.")
    # 자릿수 세기 위해서 숫자를 문자로 변경하고 len을 이용하여 길이를 알아낸다.