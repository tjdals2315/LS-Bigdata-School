import random
hangul_1 = list("강고김이박서권정추하")
hangul_2 = list("우인미강흥정성지찬감")
hangul_3 = list("인찬성원훈민석희호성")

# 파일쓰기 모드
with open('info.txt', "w") as file:
  for i in range(1000):
    # 랜덤한 값으로 변수 생성
    name = random.choice(hangul_1)+random.choice(hangul_2)+random.choice(hangul_3)
    height = random.randrange(130,200)
    weight = random.randrange(40,120)
    file.write("{}, {}, {}\n".format(name,height,weight))


# 파일 열기
file = open('info.txt', "r")
# 텍스트 읽기
contents = file.read()
print(contents)
# 파일 닫기
file.close()