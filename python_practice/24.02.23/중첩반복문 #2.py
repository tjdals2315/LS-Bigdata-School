# 전체 피라미드 (9층)
output = ""

for i in range(1, 10):
    for j in range(9, i, -1):
        output += " "
    for k in range(0, 2 * i -1):
        output += "*"
    output += "\n"

print(output)