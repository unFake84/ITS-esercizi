'''
Exercise 1
Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.
'''

def check_value(num:int):

    if num == 5:

        print(f"{num} is == 5.")
    
    elif num > 5:

        print(f"{num} is > than 5.")
    
    else:

        print(f"{num} is < than 5")

check_value((int(input("Inserire un numero intero,\nper determinare se è maggiore o uguale a 5\n: "))))