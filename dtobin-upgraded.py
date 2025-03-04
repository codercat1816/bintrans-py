try:  
  while True:
      decimal_request = input(">>> ") 
      decimal_request = int(decimal_request) 
      binary_value = bin(decimal_request)
      print(binary_value[2:])
except ValueError:
  print("Invalid Input")
  
