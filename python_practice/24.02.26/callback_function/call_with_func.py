# 함수를 선언
def power(item):
    return item * item
def under_3(item):
    return item < 3

# 변수를 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수를 사용
output_a = map(power, list_input_a)
print(output_a)
print(list(output_a))
print()

# filter() 함수를 사용
output_b = filter(under_3, list_input_a)
print(output_b)
# 함수를 선언
def power(item):
    return item * item
def under_3(item):
    return item < 3

# 변수를 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수를 사용
output_a = map(power, list_input_a)
print(output_a)
print(list(output_a))
print()

# filter() 함수를 사용
output_b = filter(under_3, list_input_a)
print(output_b)
print(list(output_b))
