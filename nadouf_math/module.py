import math



__all__ = [
    'Nadoufmath', 'number_pi', 'number_e', 'sum_of', 'division_of', 
    'int_division_of', 'multiply_of', 'square', 'cube', 'power', 
    'power_of_2', 'square_root', 'cube_root', 'factorial', 'gcd_with', 
    'lcm_with', 'floor', 'is_infinity', 'is_positive', 'is_negative', 
    'sign', 'is_even', 'is_odd', 'cos', 'sin', 'tan', 'is_pi'
]


number_pi = 3.14159265359
number_e = 2.718281828459


# functions

def sum_of(*args):
    return sum(args)

def difference_of(*args):
    if not args:
        return 0
    first = args[0]
    return first - sum(args[1:])

def division_of(*args):
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("You can't divide by zero!")
        result /= num
    return result

def int_division_of(*args):
    if not args:
        return 0
    
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("You can't divide by zero!")
        result //= num
    return result

def multiply_of(*args):
    if not args:
        return 0
        
    result = args[0]
    for num in args[1:]:
        result *= num
    return result

def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def power(number, exponent):
    return number ** exponent

def power_of_2(number):
    return 2 ** number

def square_root(number):
    return number ** 0.5

def cube_root(number):
    return number ** (1/3)

def factorial(number):
    if number < 0:
        return "The factorial of a negative number is not defined."
    if number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number+1):
            result *= i
        return result

def gcd_with(*args):
    result = args[0]
    for num in args[1:]:
        a, b = result, num
        while b:
            a, b = b, a % b
        result = a
    return result

def lcm_with(*args):
    result = abs(args[0])
    for num in args[1:]:
        num = abs(num)
        result = abs(result * num) // gcd_with(result, num)
    return result

def floor(number):
    return number//1

def is_infinity(number):
    return math.isinf(number)

def is_positive(number):
    return number > 0

def is_negative(number):
    return number < 0

def sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
        
def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

def cos(number, terms=10):
    number = number % (2 * number_pi)
    if number > number_pi:
        number -= 2 * number_pi

    result = 0
    for i in range(terms): 
        term = ((-1) ** i) * (number** (2 * i)) / factorial(2 * i)
        result += term
    return result

def sin(number, terms=10):
    number = number % (2 * number_pi)
    if number > number_pi:
        number -= 2 * number_pi
    
    result = 0
    for i in range(terms):
        term = ((-1) ** i) * (number ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result

def tan(number, terms=10):
    return sin(number, terms) / cos(number, terms)

def is_pi(number):
    return number == number_pi


# class 

class Nadoufmath:
    def __init__(self, number):
        self.number = number

    def sum_of(self, *args):
        return self.number + sum(args)
    
    def difference_of(self, *args):
        return self.number - sum(args)
    
    def division_of(self, *args):
        if not args:
            return self.number
        result = self.number
        for num in args:
            if num == 0:
                raise ValueError("You can't divide by zero!")
            result /= num
        return result
    
    def int_division_of(self, *args):
        if not args:
            return self.number
    
        result = self.number
        for num in args:
            if num == 0:
                raise ValueError("You can't divide by zero!")
            result //= num
        return result
    
    def multiply_of(self, *args):
        if not args:
            return self.number
        
        result = self.number
        for num in args:
            result *= num
        return result
    
    def square(self):
        return self.number ** 2
    
    def cube(self):
        return self.number ** 3
    
    def power(self, exponent):
        return self.number ** exponent
    
    def power_of_2(self):
        return 2 ** self.number
    
    def square_root(self):
        return self.number ** 0.5
    
    def cube_root(self):
        return self.number ** (1/3)
    
    def factorial(self):
        if self.number < 0:
            return "The factorial of a negative number is not defined."
        if self.number == 0:
            return 1
        else:
            result = 1
        for i in range(1, self.number+1):
            result *= i
        return result
    
    def gcd_with(self, *args):
        result = self.number
        for num in args:
            a, b = result, num
            while b:
                a, b = b, a % b
            result = a
        return result
    
    def lcm_with(self, *args):
        result = abs(self.number)
        for num in args:
            num = abs(num)
            result = abs(result * num) // gcd_with(result, num)
        return result
    
    def floor(self):
        if self.number >= 0:
            return self.number // 1
        else:
            return -((-self.number) // 1) - (1 if self.number % 1 != 0 else 0)
    
    def is_infinity(self):
        return math.isinf(self.number)
    
    def is_positive(self):
        return self.number > 0
    
    def is_negative(self):
        return self.number < 0
    
    def sign(self):
        if self.number > 0:
            return "Positive"
        elif self.number < 0:
            return "Negative"
        else:
            return "Zero"
        
    def is_even(self):
        return self.number % 2 == 0
    
    def is_odd(self):
        return self.number % 2 != 0
    
    def cos(self, terms=10):
        x = self.number % (2 * number_pi)
        if x > number_pi:
            x -= 2 * number_pi
        
        result = 0
        for i in range(terms): 
            term = ((-1) ** i) * (x** (2 * i)) / factorial(2 * i)
            result += term
        return result

    def sin(self, terms=10):
        x = self.number % (2 * number_pi)
        if x > number_pi:
            x -= 2 * number_pi
        
        result = 0
        for i in range(terms):
            term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
            result += term
        return result

    def tan(self, terms=10):
        return self.sin(terms) / self.cos(terms)

    def is_pi(self):
        return self.number == number_pi

