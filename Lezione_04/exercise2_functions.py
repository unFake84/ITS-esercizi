'''
Let’s try to define a function named subtract ourselves:
● It should take 2 parameters.
● Inside the function, it should subtract the two.
● Then, return the result.
After you defined it, call the function with some arguments!
'''

def subtract(a: int, b: int) -> int:

        result: int = a - b
        return result

my_result: int = subtract(4,1)
print(my_result)

#print(f"La sottrazione di a[20] e b[14] è: {subtract(20, 14)}")