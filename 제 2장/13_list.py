friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(len(friends[0]))
print(range(len(friends)))

# 리스트의 원소를 직접 사용
for friend in friends:
  print("Happy New Year :", friend)

# 리스트의 길이에 대한 범위를 사용
for i in range(len(friends)):
  friend = friends[i]
  print("Happy New Year :", friend)

# 리스트 연결 "+"
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# 리스트 메소드
stuff = list()
stuff.append('book')  # .append() 원소 추가
stuff.append(99)
print(stuff)

# d =list()
# for i in range(len(a)):
#   d.append(a[i]+b[i])
# print(d)

num = [5, 4, 3, 2, 1]
print(3 in num) # in 리스트 내 원소 존재 확인
print(6 in num)
num.sort()  # .sort() 리스트 정렬
print(num)

print(len(num)) # len() 리스트의 길이
print(min(num)) # min() 리스트 내 최소값
print(max(num)) # max() 리스트 내 최대값
print(sum(num)) # sum() 리스트 내 값들의 합

# 문자열을 리스트로 나누기
str = "Hello Python World !!!"
split_str = str.split()
print(str)
print(split_str)
for i in split_str:
  print(i)

# 특정 문자를 기준으로 문자열 나누기
str = "Hello;Python;World;!!!"
split_str = str.split(';')
print(split_str)