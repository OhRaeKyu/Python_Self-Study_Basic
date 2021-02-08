fname = input("Enter the file name : ")

if len(fname) < 1 :
  fname = "clown.txt"

xfile = open(fname, "r")

di = dict()

for line in xfile:
  line = line.rstrip()
  words = line.split() 
  for w in words:
    di[w] = di.get(w, 0) + 1

count = None
word = None
for k, v in di.items():
  if count is None or v > count:
    count = v
    word = k
print("most common word :", word, count)