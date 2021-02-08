s = "Hello World"

# 예외 처리
try :
  s = int(s)  # 예외 발생 시
except :
  s = -1  # 이부분 실행

print("First", s)

s = "123"
try :
  s = int(s)
except :
  s = -1

print("Second", s)