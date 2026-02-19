class Nadoufmath:
    def __init__(self, number):
        self.number = number
    def sum_of(self, *args):
        self.total = self.number + sum(args)
        return self.total
    def difference_of(self, *args):
        self.total = self.number - sum(args)
        return self.total
    def square(self):
        self.total = self.number ** 2
        return self.total
    def cube(self):
        self.total = self.number ** 3
        return self.total
    def power(self, power):
        self.power = power
        self.total = self.number ** self.power
        return self.total