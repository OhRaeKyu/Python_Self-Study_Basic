xfile = open("mbox-short.txt", "r")

for line in xfile:
  line = line.rstrip()
  words = line.split()
  if len(words) < 3 or words[0] != "From":
    continue
  print(words[2])
