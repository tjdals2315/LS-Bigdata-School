power = lambda x: x * x
under_3 = lambda x: x < 3

list_a = [1, 2, 3, 4, 5]

# map() function
output_a = map(power, list_a)
print(output_a)
print(list(output_a))
print()

# filter() function
output_b = filter(under_3, list_a)
print(output_b)
print(list(output_b))