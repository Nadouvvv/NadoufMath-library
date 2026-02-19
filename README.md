# Nadouf-Math Library

## Content

- [About library](#about-library)
- [Installing](#installing)
- [Fast start](#fast-start)
- [Documentation](#documentation)


## About library

A simple Python library for mathematical operations. In NadoufMath you can choose what you want - use functions or objects with methods!

## Installing THE LIBRARY IS STILL UNDER DEVELOPMENT

```bash
The library is still under development
```

## Fast start

```python
from nadouf_math import Nadoufmath

# creating an object with value 5
calc = Nadoufmath(5)

# Demonstrate arithmetic operations

print(f"Sum: {calc.sum_of(11, 12, 13, 14, 15)}")        # 5 + (11 + 12 + 13 + 14 + 15) = 70
print(f"Difference: {calc.difference_of(3, 2, 1)}")     # 5 - 3 - 2 - 1 = -1
print(f"Square: {calc.square()}")                       # 5² = 25
print(f"Cube: {calc.cube()}")                           # 5³ = 125
print(f"Power 4: {calc.power(4)}")                      # 5⁴ = 625
print(f"Square root: {calc.square_root()}")             # √5               
```

## Documentation

- [Simple mathematical operations](#simple-mathematical-operations)
- [Powers and Roots](#powers-and-roots)

## Simple mathematical operations

For sum of numbers you can use function **sum_of** or method **sum_of** for your object:
```python
from nadouf_math import *

print(sum_of(5, 6)) # if you want to use function. it will print 11

number = Nadoufmath(5)
print(number.sum_of(6)) # if you want to use the method. it will print 11 too
```



For difference of numbers you can use function **difference_of** or method **difference_of** for your object:
```python
from nadouf_math import *

print(difference_of(10, 3)) # if you want to use function. it will print 7

number = Nadoufmath(10)
print(number.difference_of(3)) # if you want to use the method. it will print 7 too
```



For division of numbers you can use function **division_of** or method **division_of** for your object:
```python
from nadouf_math import *

print(division_of(5, 5)) # if you want to use function. it will print 1

number = Nadoufmath(5)
print(number.division_of(5)) # if you want to use the method. it will print 1 too
```

For integer division you should use function **int_division_of** or method **int_division_of** for your object:
```python
from nadouf_math import *

print(int_division_of(5, 2)) # if you want to use function. it will print 2

number = Nadoufmath(5)
print(number.int_division_of(2)) # if you want to use the method. it will print 2 too
```




For multiply of numbers you can use function **multiply_of** or method **multiply_of** for your object:
```python
from nadouf_math import *

print(multiply_of(7, 8)) # if you want to use function. it will print 56

number = Nadoufmath(7)
print(number.multiply_of(8)) # if you want to use the method. it will print 56 too
```


## Powers and Roots

For square of number you can use function **square** or method **square** for your object:
```python
from nadouf_math import *

print(square(4)) # if you want to use function. it will print 16

number = Nadoufmath(4)
print(number.square()) # if you want to use the method. it will print 16 too
```



For cube of number you can use function **cube** or method **cube** for your object:
```python
from nadouf_math import *

print(cube(2)) # if you want to use function. it will print 8

number = Nadoufmath(2)
print(number.cube()) # if you want to use the method. it will print 8 too
```



For any other power of number you should use function **power** or method **power** for your object:
```python
from nadouf_math import *

print(power(2, 4)) # if you want to use function. it will print 16

number = Nadoufmath(2)
print(number.power(4)) # if you want to use the method. it will print 16 too
```



If you want to count any power of number 2 you should use function **power_of_2**:
```python
from nadouf_math import *

print(power_of_2(3)) # if you want to use function. it will print 8

```



For square root of number you have to use function **square_root** or method **square_root** for your object:
```python
from nadouf_math import *

print(square_root(64)) # if you want to use function. it will print 8

number = Nadoufmath(64)
print(number.square_root()) # if you want to use the method. it will print 8 too
```
