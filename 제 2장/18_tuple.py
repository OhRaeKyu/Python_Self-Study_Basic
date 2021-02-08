di = {"c" : 10, "a" : 1, "b" : 22}
tmp = list()
for k, v in di.items():
  tmp.append((v, k)) # (v, k) 튜플로 이루어진 리스트
print(tmp)

tmp = sorted(tmp, reverse = True)
print(tmp)

# 파일을 읽어 가장 빈도 수가 높은 단어를 찾고 정렬하기
xfile = open("intro.txt", "r")
counts = dict()
for line in xfile:
  line = line.rstrip()
  words = line.split()
  for w in words:
    counts[w] = counts.get(w, 0) + 1

lst = list()
for k, v in counts.items():
  lst.append((v, k)) # (v, k) 튜플로 이루어진 리스트

lst = sorted(lst, reverse = True)

print("-- The most common words Top 10 --")
for v, k in lst[:10]:
  print(k, v)

# 위 과정 단축 솔루션
print("** Using Sort Method **")
c = {"c" : 10, "a" : 1, "b" : 22}
print(sorted([(v, k)for k, v in c.items()], reverse = True))