# test() 함수 선언
def test():
	print("test() function's first line")
	try:
		print(" try 구문 실행되었습니다.")
		return
		print("try 구문 return 키워드 뒤입니다.")
	except:
		print("except 구문 실행되었습니다.")
	else:
		print("else 구문 실행되었습니다.")
	finally:
		print("finally 구문 실행되었습니다.")
	print("test() function's last line")
# test() 함수 호출
test()