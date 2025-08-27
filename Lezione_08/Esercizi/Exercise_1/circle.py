'''
    [2a]
    Then, create two concrete subclasses, Circle and Rectangle, that both extend the Shape class.
    Each of these subclasses must provide their own implementation of the area and perimeter methods,
    based on the geometric formulas appropriate to their shapes.
'''

from shape import Shape

# [2a]
class Circle(Shape):

    def __init__(self, raggio: int) -> None:
        super().__init__()

        self.raggio = raggio
    
    def area(self) -> int|float:
        eleva_raggio: int = self.raggio * self.raggio
        area: int|float = eleva_raggio * 3.14159

        return area
    
    def perimeter(self) -> int|float:
        diametro_cerchio: int|float = self.raggio * 2
        perimetro_cerchio: int|float = diametro_cerchio * 3.14159

        return perimetro_cerchio