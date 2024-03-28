import pandas as pd
import numpy as np

score1 = [3, 7, 5, 4, 5, 6, 7, 8, 6, 5]
score2 = [34, 54, 17.26, 34, 25, 14, 24, 25, 23]
score3 = [154, 167, 132, 145, 154, 145, 113, 156, 154, 123]

# 평균
print(sum(score1)/len(score1))
print(sum(score2)/len(score2))
print(sum(score3)/len(score3))

# 중앙값
x = pd.Series(score1)
x1 = x.sort_values()
print(x1[5] + x1[6]/2)


# 최빈값