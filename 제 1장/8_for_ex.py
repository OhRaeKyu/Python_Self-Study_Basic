total = 0
count = 0
average = 0

while True:
  numbers = input("Enter a number : ")
  if numbers == "done" :
    break
  else :
    try :
      numbers = float(numbers)
      total += numbers
      count += 1

    except :
      print("Invalid input")
      continue

average = total / count
print(total, count, average)