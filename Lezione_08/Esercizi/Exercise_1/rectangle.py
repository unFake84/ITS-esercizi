'''
    [2b]
    Then, create two concrete subclasses, Circle and Rectangle, that both extend the Shape class.
    Each of these subclasses must provide their own implementation of the area and perimeter methods,
    based on the geometric formulas appropriate to their shapes.
'''

from shape import Shape

# [2b]
class Rectangle(Shape):

    def __init__(self, altezza: int|float, larghezza: int|float) -> None:
        super().__init__()

        self.altezza = altezza
        self.larghezza = larghezza
    
    def area(self) -> int|float:
        formula: int|float = self.altezza * self.larghezza

        return formula
    
    def perimeter(self) -> int|float:
        formula: int|float = (self.altezza * 2) + (self.larghezza * 2)

        return formula