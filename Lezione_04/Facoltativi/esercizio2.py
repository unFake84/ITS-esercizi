'''
Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is
    too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or
    reaches the maximum number of attempts.

'''

import random

def randomNumber( x:int, y:int ) -> int | None:

    if x < y:
        z: int = random.randint( x, y )

        return z
    
    else:

        return None

if __name__ == "__main__":

    user: str = ""
    attempts: int = 0
    victory: bool = False

    while True:

        user = input( "Insert first integer number: " )

        try:
            x: int = int( user )
            break

        except ValueError:
            print( "Must be an integer." )
            continue

    while True:

        user = input( "Insert second integer number: " )

        try:
            y: int = int( user )
            if y <= x:
                print( f"Second number must be higher than first! -> { x }." )
                continue
            break

        except ValueError:
            print( "Must be an integer." )
            continue

    while True:

        user = input( "Insert attempts (integer): " )

        try:
            attempts = int( user )
            if attempts <= 0:
                print( "Must be greater than 0." )
                continue
            break

        except ValueError:
            print( "Must be an integer." )
            continue

    print( "GAME BEGUN! FIND A HIDDEN NUMBER!" )
    hidden_number: int = randomNumber( x, y )

    for attempt in range( attempts ):

        user = input( f"Guess the number? attempt { attempt + 1 } of { attempts }: " )

        try:
            userint: int = int( user )
            if userint == hidden_number:
                print( "NUMBER FOUND! CONGRATULATIONS!!!" )
                victory = True
                break

            elif userint < hidden_number:
                print( "Too low!" )

            elif userint > hidden_number:
                print( "Too high!" )

        except ValueError:
            print( "It's not an integer! You still lost one attempt." )

    if not victory:
        print( f"You lost, the number to find was: { hidden_number }" )

    print( "Game over" )