from abc import ABC, abstractmethod

# [1]
class Shape(ABC):

    @abstractmethod
    def area(self) -> int|float:
        pass
    
    @abstractmethod
    def perimeter(self) -> int|float:
        pass