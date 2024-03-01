list_a = [1, 2, 3, 4, 5,]

# map() function
output_a = map(lambda x: x * x, list_a) # power() 함수를 선언하지 않고, 매개변수로 바로 넣을 수 있다.
print(output_a)
print(list(output_a))

# filter() function
output_b = filter(lambda x: x < 3, list_a)
print(output_b)
print(list(output_b))