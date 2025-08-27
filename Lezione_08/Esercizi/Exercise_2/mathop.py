'''
    [1]
    Create a class called MathOperations to group together some basic arithmetic functionality.
    Inside this class, define two static methods:

    add, which accepts two numeric parameters and returns their sum.
    multiply, which also takes two numeric parameters and returns their product.
'''

# [1]
class MathOperations:

    @staticmethod
    def add(a: int|float, b: int|float) -> int|float:
        return a + b
    
    @staticmethod
    def multiply(a: int|float, b: int|float) -> int|float:
        return a * b