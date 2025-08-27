'''
    [1]
    Start by defining an abstract base class called Shape.
    This class should include two abstract methods: one named area,
    which will be responsible for calculating the area of a shape,
    and another named perimeter, which will calculate the perimeter.

    Since Shape is abstract, it will not provide specific implementations for these methods.
    Instead, it sets a blueprint for all shapes that will inherit from it.
'''

from abc import ABC, abstractmethod

# [1]
class Shape(ABC):

    @abstractmethod
    def area(self) -> int|float:
        pass
    
    @abstractmethod
    def perimeter(self) -> int|float:
        pass