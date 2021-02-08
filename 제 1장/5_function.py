def computepay(hours, rate) :
  pay = hours * rate

  if hours > 40 :
    pay += (hours - 40) * rate / 2
  
  return pay

hours = input("Enter Hours : ")
rate = input("Enter Rate : ")

hours = float(hours)
rate = float(rate)

print("Pay :", computepay(hours, rate))