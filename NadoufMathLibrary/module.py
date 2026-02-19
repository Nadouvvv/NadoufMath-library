import math

class Nadoufmath:
    def __init__(self, number):
        self.number = number
    def sum_of(self, *args):
        return self.number + sum(args)
    def difference_of(self, *args):
        return self.number - sum(args)
    def square(self):
        return self.number ** 2
    def cube(self):
        return self.number ** 3
    def power(self, power):
        self.power = power
        return self.number ** self.power
    def square_root(self):
        return math.sqrt(self.number)
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
