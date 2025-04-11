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

# 1.
def validate_password(password: str):

    uppercase: int = 0

    for char in password:

        if char.upper() in password:

            uppercase += 1

    if len(password) > 20:

        print("Errore, the password must be minimum lenght of 20 characters")