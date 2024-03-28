# 문제1
score1 = pd.Series([3, 7, 5, 4, 5, 6, 7, 8, 6, 5])
score2 = pd.Series([34, 54, 17, 26, 34, 25, 14, 24, 25, 23])
score3 = pd.Series([154, 167, 132, 145, 154, 145, 113, 156, 154, 123])

# 평균
print(score1.mean(), score2.mean(), score3.mean())

# 중앙값
print(score1.median(), score2.median(), score3.median())

# 최빈값
print(score1.value_counts(), score2.value_counts(), score3.value_counts())

print(mode_mtp(score1), mode_mtp(score2), mode_mtp(score3))