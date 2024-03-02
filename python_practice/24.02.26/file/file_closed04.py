try:
    file = open("info.txt", "w")
    # 작업 수행할 코드
    예외
except:
    print("오류 발생")

# except이 끝나고 닫으면 문제없음
file.close()
print("# 파일 제대로 닫혔는지 확인")
print("file.close: ", file.closed)