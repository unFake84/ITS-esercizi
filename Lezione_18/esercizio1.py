'''
Safe Square Root:

1.
    Write a function safe_sqrt(number) that
    calculates the square root of a number using math.sqrt().
    
2.
    Handle ValueError if the input is negative by returning an informative message.

'''

from math import sqrt

def safe_sqrt(number):

    try:

        square_root: float = sqrt(number)

        return square_root

    except ValueError:

        return f"It cannot be done."
    
if __name__ == "__main__":

    print("\n\tCalculates the square root of a number.")
    print("\tEnter '0' to exit at any time.\n")

    while True:

        try:

            user: float = (float(input("Enter a number: ")))

            if user == 0:
                
                print("\nYou pressed '0'.\n\n\t Closing application.\n")
                break

        except ValueError:

            print(f"It is a string!\n\n\tResult: A string cannot be calculated \n")

            continue  

        salva = safe_sqrt(user)
        print(f"\n\tResult: {salva} \n")