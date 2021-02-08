# 1부터 5까지 출력
for i in [1, 2, 3, 4, 5] :
  print(i)

# range() 범위 리스트 생성
print("range")
for i in range(1,6) :
  print(i)

# 최대 값 구하기
largest = 0
print("Before :", largest)

numbers = [9, 41, 12, 3, 74, 15]

for i in numbers :
  if i > largest :
    largest = i
  print("largest :", largest, "current :", i)

print("After :", largest)
  