with open('info.txt', "r") as file:
  for line in file:
    name, height, weight = line.strip().split(", ") 
    if (not name) or (not height) or (not weight):
      continue
   
    bmi = int(weight) / (int(height)/100)**2
    result = ""
   
    if bmi >= 25:
      result = "과체중"
    elif bmi >= 18.5:
      result = "정상"
    else:
      result = "저체중"
# 출력 결과를 다음 줄로 넘기면서 사용하는 방법
      
    print("\n".join(["이름: {}",
                     "키: {}",
                     "몸무게: {}",
                     "BMI: {}",
                     "결과: {}"]).format(name,height,weight,bmi,result))