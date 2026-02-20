# Nadouf-Math Library

## Content

- [About library](#about-library)
- [Installing](#installing)
- [Import](#import)
- [Fast start](#fast-start)
- [Documentation](#documentation)


## About library

A simple Python library for mathematical operations. In NadoufMath you can choose what you want - use functions or objects with methods!

## Installing 

```bash
pip install nadouf-math
```

## Import

```python
from nadouf_math import *
```
All the following examples assume that you entered this string at the beginning.

## Fast start

```python
from nadouf_math import Nadoufmath

# Creating an object with value 5
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
- [Higher-order mathematical functions](#higher-order-mathematical-functions)
- [Trigonometry](#trigonometry)
- [Rounding](#rounding)
- [Checking the properties of numbers](#checking-the-properties-of-numbers)
- [Constants](#constants)
- [End of the documentation](#end-of-documentation)

## Simple mathematical operations


For sum of numbers you can use function **sum_of** or method **sum_of** for your object:
```python
print(sum_of(5, 6)) # if you want to use function. it will print 11

number = Nadoufmath(5)
print(number.sum_of(6)) # if you want to use the method. it will print 11 too
```



For difference of numbers you can use function **difference_of** or method **difference_of** for your object:
```python
print(difference_of(10, 3)) # if you want to use function. it will print 7

number = Nadoufmath(10)
print(number.difference_of(3)) # if you want to use the method. it will print 7 too
```



For division of numbers you can use function **division_of** or method **division_of** for your object:
```python
print(division_of(5, 5)) # if you want to use function. it will print 1

number = Nadoufmath(5)
print(number.division_of(5)) # if you want to use the method. it will print 1 too
```

For integer division you should use function **int_division_of** or method **int_division_of** for your object:
```python
print(int_division_of(5, 2)) # if you want to use function. it will print 2

number = Nadoufmath(5)
print(number.int_division_of(2)) # if you want to use the method. it will print 2 too
```




For multiply of numbers you can use function **multiply_of** or method **multiply_of** for your object:
```python
print(multiply_of(7, 8)) # if you want to use function. it will print 56

number = Nadoufmath(7)
print(number.multiply_of(8)) # if you want to use the method. it will print 56 too
```


## Powers and Roots

For square of number you can use function **square** or method **square** for your object:
```python
print(square(4)) # if you want to use function. it will print 16

number = Nadoufmath(4)
print(number.square()) # if you want to use the method. it will print 16 too
```



For cube of number you can use function **cube** or method **cube** for your object:
```python
print(cube(2)) # if you want to use function. it will print 8

number = Nadoufmath(2)
print(number.cube()) # if you want to use the method. it will print 8 too
```



For any other power of number you should use function **power** or method **power** for your object:
```python
print(power(2, 4)) # if you want to use function. it will print 16

number = Nadoufmath(2)
print(number.power(4)) # if you want to use the method. it will print 16 too
```



If you want to count any power of number 2 you should use function **power_of_2**:
```python
print(power_of_2(3)) # if you want to use function. it will print 8
```



For square root of number you have to use function **square_root** or method **square_root** for your object:
```python
print(square_root(64)) # if you want to use function. it will print 8

number = Nadoufmath(64)
print(number.square_root()) # if you want to use the method. it will print 8 too
```



If you want to count cube root of number you should use function **cube_root** or method **cube_root** for your object:
```python
print(cube_root(125)) # if you want to use function. it will print 5

number = Nadoufmath(125)
print(number.cube_root()) # if you want to use the method. it will print 5 too
```


## Higher-order mathematical functions

For factorial of number you need to use the function **factorial** or method **factorial** for your object:
```python
print(factorial(3)) # if you want to use function. it will print 6

number = Nadoufmath(3)
print(number.factorial()) # if you want to use the method. it will print 6 too
```



If you want to count the greatest common divisor you can use the function **gcd_with** or method **gcd_with** for your object:
```python
print(gcd_with(5, 10)) # if you want to use function. it will print 5

number = Nadoufmath(5) 
print(number.gcd_with(10)) # if you want to use the method. it will print 5 too
```


If you need to count the least common multiple you should use the function **lcm_with** or method **lcm_with** for your object:
```python
print(lcm_with(20, 30)) # if you want to use function. it will print 60

number = Nadoufmath(20)
print(number.lcm_with(30)) # if you want to use the method. it will print 60 too
```



## Trigonometry
Trigonometry in nadouf-math library counts in radians!


For a cosine of an angle you should use the function **cos** or the method **cos** for your object:
```python
print(cos(0.1)) # if you want to use function. it will print 0.9950041652780258

number = Nadoufmath(0.1)
print(number.cos()) # if you want to use the method. it will print 0.9950041652780258 too
```



For a sine of an angle you should use the function **sin** or the method **sin** for your object:
```python
print(sin(0.3)) # if you want to use function. it will print 0.29552020666133955

number = Nadoufmath(0.3)
print(number.sin()) # if you want to use the method. it will print 0.29552020666133955 too
```


For a tangent of an angle you should use the function **tan** or the method **tan** for your object:
```python
print(tan(0.2)) # if you want to use function. it will print 0.2027100355086725

number = Nadoufmath(0.2)
print(number.tan()) # if you want to use the method. it will print 0.2027100355086725 too
```

## Rounding

For usual round you can use the integrated function **round** in Python.

For round down you need to use the function **floor** or the method **floor** for your object:
```python
print(floor(5.9)) # if you want to use function. it will print 5

number = Nadoufmath(5.9)
print(number.floor()) # if you want to use the method. it will print 5 too
```



For round up you need to use the function **ceil** or the method **ceil** for your object:
```python
print(ceil(5.2)) # if you want to use function. it will print 6

number = Nadoufmath(5.2)
print(number.ceil()) # if you want to use the method. it will print 6 too
```


## Checking the properties of numbers

If you want to compare number with infinity you should use the function **is_infinity** or the method **is_infinity** for your object:
```python
print(is_infinity(5)) # if you want to use function. it will print False

number = Nadoufmath(5)
print(number.is_infinity()) # if you want to use the method. it will print False too
```


If you want to check number is positive or negative you can use functions **is_positive**, **is_negative** or methods **is_positive** and **is_negative** for your object:
```python
print(is_positive(-6)) # if you want to use function. it will print False
print(is_negative(-3)) # if you want to use function. it will print True

number_1 = Nadoufmath(-6)
number_2 = Nadoufmath(-3)
print(number_1.is_positive()) # if you want to use the method. it will print False too
print(number_2.is_negative()) # if you want to use the method. it will print True too
```

To find out the sign of a number use the function **sign** or the method **sign** for your object:
```python
print(sign(6)) # if you want to use function. it will print Positive

number = Nadoufmath(6)
print(number.sign()) # if you want to use the method. it will print Positive too
```

To check parity of a number use functions **is_even**, **is_odd** or use methods **is_even** and **is_odd** for your objects:
```python
print(is_even(79)) # if you want to use function. it will print False
print(is_odd(67)) # if you want to use function. it will print True

number = Nadoufmath(79)
print(number.is_even()) # if you want to use the method. it will print False too
print(number.is_odd()) # if you want to use the method. it will print True
```

## Constants

To use number Pi use variable **number_pi**:
```python
print(number_pi) # it will print 3.14159265359
```


To use number E use variable **number_e**:
```python
print(number_e) # it will print 2.718281828459
```


## End of the documentation
All the functions of the Nadouf-Mathematica library were described in the documentation. Thanks for reading!