try:
    file = open("info.txt", "w")
    # 작업할 코드 입력
    예외
except:
    print("오류 발생")
finally:
    file.close()
    print("# 파일 제대로 닫혔는지 확인")
    print("file.close: ", file.closed)