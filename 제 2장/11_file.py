# 파일 열기 - 읽기 모드 "r"
xfile = open("2016039080_오래규.txt", "r")
for line in xfile :
  print(line)

# 파일의 줄 수 세기
xfile = open("2016039080_오래규.txt", "r")
count = int(0)
for line in xfile :
  count += 1
print("Line Count :", count)

# 파일을 하나의 문자열로 읽기
xfile = open("2016039080_오래규.txt", "r")
inp = xfile.read()
print(len(inp))
print(inp[:20])

# 원하는 문자가 포함된 문자열 찾기_1
xfile = open("2016039080_오래규.txt", "r")
for line in xfile :
  line = line.rstrip()
  if not line.startswith("From :"):
    continue
  print(line)

# 원하는 문자가 포함된 문자열 찾기_2
xfile = open("2016039080_오래규.txt", "r")
for line in xfile:
  line = line.rstrip()
  if not 'From :' in line:
    continue
  print(line)

# 파일명 입력 받아
fname = input("Enter the file name : ")
try:
  xfile = open(fname)
except:
  print("File cannot be opened", fname)
  quit()

count = 0
for line in xfile:
  if line.startswith("From :"):
    count += 1
print("There were", count, "subject lines in", fname)