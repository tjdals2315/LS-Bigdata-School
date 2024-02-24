# 1부터 숫자를 하나씩 증가시키면서 더하는 경우에, 몇을 더할 때 10000을 넘는지 구하고 그때의 값을 출력해보시오.
limit = 10000
i = 1

sum_value = 0
while sum_value < limit:
    sum_value = sum_value + i
    i = i + 1
    
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_value))