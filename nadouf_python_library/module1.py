import random

class Math:
    def __init__(self, number):
        self.number = number
    def sum_of(self, *args):
        self.total = 0
        self.total = self.number + sum(*args)