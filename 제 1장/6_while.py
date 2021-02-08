n = 0

# 1부터 5까지 출력
while n < 5 :
  print(n+1)
  n += 1

# break & continue
while True :
  line = input(">")
  if line == "done" :
    break
  if line[0] == "#" :
    continue
  print(line)
print("Done !")
