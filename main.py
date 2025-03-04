from sbin import sbin

try:  
  while True:
      print(sbin(input(">>>")))
except ValueError:
  print("Invalid Input")
  
