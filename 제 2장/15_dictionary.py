# 딕셔너리 생성_1
dic_1 = dict()
dic_1["key_1"] = 10
dic_1["key_2"] = 20
print(dic_1)

# 딕셔너리 생성_2
dic_2 = {"key_1" : 100, "key_2" : 200}
print(dic_2)

# 카운팅 예제_1
# "key" in dictionary 딕셔너리에서 특정 key 값이 존재하는지 찾기
counts = dict()
names = ["aaa", "bbb", "ccc", "aaa", "bbb", "ddd"]
for name in names:
  if name not in counts:  # key 값이 존재하지 않으면
    counts[name] = 1      # 새로운 딕셔너리 추가
  else :
    counts[name] += 1     # 존재 시 카운팅 + 1
print("counting_1 :", counts)

#카운팅 예제_2
counts = dict()
names = ["aaa", "bbb", "ccc", "aaa", "bbb", "ddd"]
for name in names:
  counts[name] = counts.get(name,0) + 1 # get("finding key", default value)
print("counting_2 :",counts)

# 딕셔너리 메소드
print(counts.keys())    # 키 값의 리스트
print(counts.values())  # 벨류 값의 리스트
print(counts.items())   # 키, 벨류 쌍의 리스트

for x, y in counts.items(): # 반복 변수로 키, 벨류 사용
  print(x, y)