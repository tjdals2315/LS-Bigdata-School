# try ~ except
try:
     file = open("info.txt", "w")
     # 작업 수행할 코드 입력
     file.close()

except:
     print("오류 발생")

print("# 파일 제대로 닫혔는지 확인")
print("file.close: ", file.closed)