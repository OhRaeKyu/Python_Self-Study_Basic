fname = input("Enter the file name : ")
xfile = open(fname, "r")

counts = dict()
for line in xfile:
  line = line.rstrip()
  words = line.split()
  for w in words:
    counts[w] = counts.get(w, 0) + 1

result_lst = sorted([(v, k) for k, v in counts.items()], reverse = True)
# print(result_lst[:5])

for k, v in result_lst[:5]:
  print(k, v)