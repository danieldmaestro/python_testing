class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, right):
        return Complex(self.real + right.real, self.imaginary + right.imaginary)
    
    def __iadd__(self, right):
        self.real += right.real
        self.imaginary += right.imaginary
        return self
    
    def __repr__(self) -> str:
        return (f"({self.real} " +
                ('+' if self.imaginary >= 0 else '-') + 
                f' {abs(self.imaginary)}i)')

# x = Complex(real=2, imaginary=4)
# y = Complex(real=5, imaginary=-1)

# x += y
# print(x)

# NAMED TUPLES. some weird type of class and object behavior
# from collections import namedtuple

# Card = namedtuple("Card", ['face', 'suit'])

# card = Card(face='Ace', suit='Spades')
# card = Card._make(['Queen', 'Hearts'])
# card2 = Card._make(['King', 'Clubs'])
# print(card.face)
# print(card.suit)
# print(card2.suit)
# print(card2.face)

from dataclasses import dataclass
from typing import ClassVar,List

@dataclass
class Card:
    FACES : ClassVar[List[str]] = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King']
    SUITS : ClassVar[List[str]] = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

