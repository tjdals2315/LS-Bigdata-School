try:
    file = open("info.txt", "w")
    # 작업할 코드 작성
    예외
    file.close()

except:
    print("오류가 발생했습니다.")

print("# 파일 제대로 닫혔는지 확인")
print("file.close: ", file.closed)