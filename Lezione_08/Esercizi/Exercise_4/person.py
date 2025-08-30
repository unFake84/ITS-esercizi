'''
    [1]
    Create an abstract class Person:
    Attributes:

        name
        age

    Methods:

        get_role, an abstract method to be implemented by subclasses.
        __str__, method to return a string representation of the person.

'''

from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{'Name:':<12} {self.name:<10}\n{'Age:':<12} {self.age:<10}\n"