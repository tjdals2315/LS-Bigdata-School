max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - i

    multiple = i * j
    if max_value < multiple:
        a = i
        b = j
        max_value = multiple
print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

# # In the context of your code, the while loop is unnecessary because it doesn't serve any real purpose. 
# The loop condition while max_value < multiple implies that the loop will continue executing as long as max_value is less than multiple. 
# However, the loop doesn't contain any statements that modify the values of max_value, a, or b within its body. 
# Therefore, if the loop ever starts, it will keep executing indefinitely, which is not what you want in this case.

# # Instead, you can use an if statement since you only need to check once whether the current multiple is greater than the current max_value. 
# If it is, you update the values of a, b, and max_value. There's no need for continuous checking using a while loop.