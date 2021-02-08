# 파일을 불러와 각 단어 카운팅하기
xfile = open("counting.txt", "r")
counts = dict()
for line in xfile:
  line = line.strip()
  line_str = line.split()
  for word in line_str:
    counts[word] = counts.get(word, 0) + 1
print("---Counting List---\n", counts)

bigcount = None
bigword = None
for word, count in counts.items():
  if bigcount is None or count > bigcount:
    bigcount = count
    bigword = word

print("Most used word :", bigword, bigcount)