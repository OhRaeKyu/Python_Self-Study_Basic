# 문자열의 길이 len()
fruit = "banana shake"
print(len(fruit))

# 특정 문자의 수 계산
count = 0
for i in fruit :
  if i == "a" :
    count += 1
print("Count of 'a' :", count)

# 문자의 시작 위치 탐색
find_str = fruit.find("na")
print("Start point of 'na' :", find_str)

# 대소문자 변경
upper_str = fruit.upper()
lower_str = fruit.lower()
print("Upper to string :", upper_str)
print("Lower to string :", lower_str)

# 문자열 대체
replace_str = fruit.replace("banana", "strawberry")
print("Replace to string :", replace_str)

# 문자열의 시작 문자 비교
print(fruit.startswith("banana"))
print(fruit.startswith("strawberry"))

# 공백 삭제
fruit = "   banana shake      "
print("Left strip :", fruit.lstrip())
print("Right strip :", fruit.rstrip())
print("Strip :", fruit.strip())

# 예제 (이메일에서 학교 주소 추출하기)
data = "From stephen.marquard@uct.ac.za Sat jan 5 09:14:16 2008"
atpos = data.find("@")
sppos = data.find(" ", atpos)
find_data = data[atpos + 1 : sppos]
print(find_data)