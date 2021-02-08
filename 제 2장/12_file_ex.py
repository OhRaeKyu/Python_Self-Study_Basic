fh = open("mbox-short.txt", "r")
for line in fh:
  line = line.rstrip()
  print(line.upper())