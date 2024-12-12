
"""
Decimal to Binary Converter

Author: Azlaan Jawed
Username: Codercat
Date: 04/12/2024
"""
# Decimal work
decimal_request = input("Decimal to Binary: ") 
decimal_request = int(decimal_request) 

# Binary work
binary_value = bin(decimal_request)

# Printing the binary value
print(binary_value[2:])
