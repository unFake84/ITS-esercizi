'''
Password Validation 1:

1.
    Write a function validate_password(password)
    that checks whether a password meets the 
    following criteria: Minimum length of 20 characters,

2.
    At least three uppercase letters,

3.
    At least four special characters (non-alphanumeric).

4.
    If the password is valid, the function should return True.

5.
    If the password is invalid,
    the function should raise a built-in exception (e.g., ValueError)
    with a message indicating which criteria were not met.

'''

import string

# 1.
def validate_password(password: str):

    uppercase: int = 0
    specialcase: int = 0

    if len(password) < 20:

        # 5a.
        raise ValueError("Error, the password must be at least 20 characters long.")

    # 2.
    for char in password:

        if char.isupper():

            uppercase += 1

        # 3.
        if char in string.punctuation:

            specialcase += 1

    # 2a.
    if uppercase < 3:

        # 5b.
        raise ValueError("Error, the password must contain at least three uppercase letters.")

    # 3a.
    if specialcase < 4:

        # 5c.
        raise ValueError("Error, the password must contains at least four special characters")

    # 4.
    return True

if __name__ == "__main__":

    print("\n\tCHANGING PASSWORD:\n")
    print("\n\tThe password must contains at least four special characters.")
    print("\tThe password must contain at least three uppercase letters.")
    print("\tThe password must be at least 20 characters long.\n")

    while True:

        try:

            user: str = (input("Insert a new password:")) # .strip()) per rimuovere gli spazi inizio&fine
            validate_password(user)
            break

        except ValueError as fnc_error:

            print(fnc_error)

    print("Changing Password Complete!")

    print("Done.")