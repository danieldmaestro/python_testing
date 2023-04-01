import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __add__(self, other):
        lcm = abs(self.denominator * other.denominator) // math.gcd(self.denominator, other.denominator)
        num_self = (lcm/self.denominator) * self.numerator
        num_other = (lcm/other.denominator) * other.numerator
        numerator = num_self + num_other
        return Fraction(numerator, lcm) 
    
    def __sub__(self, other):
        lcm = abs(self.denominator * other.denominator) // math.gcd(self.denominator, other.denominator)
        num_self = (lcm/self.denominator) * self.numerator
        num_other = (lcm/other.denominator) * other.numerator
        numerator = num_self - num_other
        return Fraction(numerator, lcm)
     
    def __mul__(self, other):
        numerator = self.numerator * other.numerator 
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __truediv__(self, other):
        numerator = self.numerator * other.denominator 
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)
    
    def __str__(self):
        return f"{int(self.numerator)}/{int(self.denominator)}"
    
a = Fraction(1,2)
b = Fraction(1,4)

print(a+b)
