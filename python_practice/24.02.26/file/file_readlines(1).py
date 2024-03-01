with open('info.txt', "r") as file:
  for line in file:
    # 변수 선언
    name, height, weight = line.strip().split(", ") # 문자열을 분리하여 리스트 형태로 반환

    # 데이터 문제 없는지 확인: 3 개의 변수에 값이 하나라도 없으면(문제) 다음 행으로 넘어감(contine)
    if (not name) or (not height) or (not weight): 
      continue
    
    # 결과 계산
    bmi = int(weight) / (int(height)/100)**2 # 값들을 숫자로 변경해줘야 함
    result = ""
   
    if bmi >= 25:
      result = "과체중"
    elif bmi >= 18.5:
      result = "정상"
    else:
      result = "저체중"
    
    # 출력
    print("이름: {}, 키: {}, 몸무게: {}, BMI: {}, 결과: {}".format(name, height, weight, bmi, result))