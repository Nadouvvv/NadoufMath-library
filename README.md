# NadoufMathLibrary

## Content

- [About library](#about-library)
- [Installing](#installing)
- [Fast start](#fast-start)
- [Documentation](#documentation)


## About library

A simple Python library for mathematical operations. In NadoufMath you can to choose that you want - use functions or objects with methods!

## Installing

```bash
pip install nadouf-math
```

## Fast start

```python
from NadoufMath import Nadoufmath

# creating an object with value 5
calc = NadoufMath(5)

# Demonstrate arithmetic operations

print(f"Sum: {calc.sum_of(11, 12, 13, 14, 15)}")        # 5 + (11 + 12 + 13 + 14 + 15) = 70
print(f"Difference: {calc.difference_of(3, 2, 1)}")     # 5 - 3 - 2 - 1 = -1
print(f"square: {calc.square()}")                       # 5² = 25
print(f"Cube: {calc.cube()}")                           # 5³ = 125
print(f"Power 4: {calc.power(4)}")                      # 5⁴ = 625
print(f"Square root: {calc.square_root()}")             # √5               
```

## Documentation

- [Simple matematical operations](#1-simple-mathematical-operations)

## 1. Simple mathematical operations

For sum of numbers you can use function sum_of or method sum_of for your object:
```python
from NadoufMath import *

print(sum_of(5, 6)) # if you want to use function. it will print 11

number = Nadoufmath(5)

print(number.sum_of(6)) # if you want to use the method. it will print 11 too
```



For difference of numbers you can use fucntion difference_of or method difference_of for your object:
```python
from NadoufMath import *

print(difference_of(10, 3)) # if you want to use function. it will print 7

number = Nadoufmath(10)

print(number.difference_of(3)) # if you want to use the method. it will print 7 too
```



For devision of numbers you can use functon devision_of or method difference_of for your object:
```python
from NadoufMath import *

print(devision_of(5, 5)) # if you want to use function. it will print 1

number = Nadoufmath(5)
print(number.devision_of(5)) # if you want to use the method. it will print 1 too
```