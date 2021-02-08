hours = input("Enter your hours : ")
rate = input("Enter your rate : ")

try :
  hours = float(hours)
  rate = float(rate)
except :
  print("입력 자료형 오류")
  quit()

pay = hours * rate

if hours > 40 :
  pay += (rate * (hours-40)) / 2

print("Your Pay :", pay)