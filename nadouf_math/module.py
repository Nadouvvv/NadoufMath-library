import math



__all__ = [
    'Nadoufmath', 'number_pi', 'number_e', 'sum_of', 'division_of', 
    'int_division_of', 'multiply_of', 'square', 'cube', 'power', 
    'power_of_2', 'square_root', 'cube_root', 'factorial', 'gcd_with', 
    'lcm_with', 'floor', 'is_infinity', 'is_positive', 'is_negative', 
    'sign', 'is_even', 'is_odd', 'cos', 'sin', 'tan', 'is_pi'
]


number_pi = math.pi
number_e = math.e



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
def power(number, power):
        return number ** power
def power_of_2(number):
        return 2 ** number
def square_root(number):
        return math.sqrt(number)
def cube_root(number):
        return math.cbrt(number)
def factorial(number):
        return math.factorial(int(round(number)))
def gcd_with(*args):
        result = args[0]
        for num in args:
            a, b = result, num
            while b:
                a, b = b, a % b
            result = a
        return result
def lcm_with(*args):
        result = abs(args[0])
        for num in args:
            num = abs(num)
            result = abs(result * num) // math.gcd(result, num)
        return result
def floor(number):
        return math.floor(number)
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
        return number%2==0
def is_odd(number):
        return number%2!=0
def cos(number):
        return math.cos(number)
def sin(number):
        return math.sin(number)
def tan(number):
        return math.tan(number)
def is_pi(number):
        return number == math.pi


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
    def power(self, power):
        return self.number ** power
    def power_of_2(self):
        return 2 ** self.number
    def square_root(self):
        return math.sqrt(self.number)
    def cube_root(self):
        return math.cbrt(self.number)
    def factorial(self):
        return math.factorial(int(round(self.number)))
    def round(self):
        return round(self.number)
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
            result = abs(result * num) // math.gcd(result, num)
        return result
    def floor(self):
        return math.floor(self.number)
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
        return self.number%2==0
    def is_odd(self):
        return self.number%2!=0
    def cos(self):
        return math.cos(self.number)
    def sin(self):
        return math.sin(self.number)
    def tan(self):
        return math.tan(self.number)
    def is_pi(self):
        return self.number == math.pi