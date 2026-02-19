from NadoufMath import Nadoufmath


number = Nadoufmath(5)


# Demonstrate arithmetic operations

print("Sum", number.sum_of(11, 12, 13, 14, 15))  # 5+11+12+12+13+14+15
print("Difference", number.difference_of(3, 2, 1)) # 5+3+2+1
print("Square",  number.square()) # 5**2
print("Cube", number.cube()) # 5**3
print("Power of number", number.power(4)) #5**4 