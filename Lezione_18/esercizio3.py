'''
Password Validation 2:

1.
    Write a function validate_password(password)
    that checks if a password meets certain criteria
    (i.e., minimum length of 20 characters, 
    at least three uppercase characters,
    and at least four special characters).

2.
    Raise a custom exception (e.g., InvalidPasswordError)
    for invalid passwords.

'''

# 2.
class InvalidPasswordError(Exception):

    pass

# 1.

import string

# 1.
def validate_password(password: str):

    uppercase: int = 0
    specialcase: int = 0

    if len(password) < 20:

        # 5a.
        raise InvalidPasswordError("Error, the password must be at least 20 characters long.")

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
        raise InvalidPasswordError("Error, the password must contain at least three uppercase letters.")

    # 3a.
    if specialcase < 4:

        # 5c.
        raise InvalidPasswordError("Error, the password must contains at least four special characters")

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

        except InvalidPasswordError as fnc_error:

            print(fnc_error)

    print("Changing Password Complete!")

    print("Done.")