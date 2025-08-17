'''
Password Generator:

    Create a function that generates a random password with a specified length
    and desired character types (lowercase letters, uppercase letters, numbers, symbols).
    Allow the user to specify the password length and desired character types.
    Generate and return a random password that meets the user's criteria.

'''

from string import ascii_lowercase, ascii_uppercase, punctuation
import random

def randomPassword(lng: int, low: str = None, upp: str = None, num: str = None, sym:str = None) -> str:

    if lng < 4:
        raise ValueError("The password length must be at least 4.")

    numbers: str = "0123456789"
    pool: str = ""
    password: str = ""
    list_password: list[str] = []

    if low is None and upp is None and num is None and sym is None:
        pool += numbers + ascii_lowercase + ascii_uppercase + punctuation

        for _ in range(lng):
            password += random.choice(pool)
        return password

    if low:
        pool += ascii_lowercase
        password += random.choice(ascii_lowercase)
        lng -= 1

    if upp:
        pool += ascii_uppercase
        password += random.choice(ascii_uppercase)
        lng -= 1

    if num:
        pool += numbers
        password += random.choice(numbers)
        lng -= 1

    if sym:
        pool += punctuation
        password += random.choice(punctuation)
        lng -= 1

    for _ in range(lng):
        password += random.choice(pool)

    list_password = list(password)
    random.shuffle(list_password)
    password = ''.join(list_password)

    return password

if __name__ == "__main__":

    user: str = ""
    lng: int = 0
    low: str = None
    upp: str = None
    num: str = None
    sym: str = None
    user_list: list[str] = []
    invalid: bool = False

    print("PASSWORD GENERATOR")
    print("Generates a random password with a specified length\nand desired character types (lowercase letters, uppercase letters, numbers, symbols).")

    while True:

        user = input("Would you like to create a password? Type 'y' or 'n': ").strip()
        invalid = False
        low = None
        upp = None
        num = None
        sym = None

        if user == 'n':
            print("\nExit")
            break

        elif user == 'y':
            user = input("Set password length, no less than 4: ").strip()

            if user.isdigit():
                if int(user) >= 4:
                    lng = int(user)
                    print("Selection:")
                    print("Press 0 to create a password immediately.")
                    print("Press 1 to create a lowercase password.")
                    print("Press 2 to create a uppercase password.")
                    print("Press 3 to create a numbers password.")
                    print("Press 4 to create a symbols password.")
                    print("Or enter the numbers in sequence to select them.")
                    user = input(">>")

                    match user:

                        case "0":
                            print("generated password")
                            print(randomPassword(lng, None, None, None, None))

                        case _:
                            if user.isdigit():
                                user_list = list(user)

                                for i in user_list:

                                    if i not in "1234":
                                        print("Invalid selection")
                                        invalid = True
                                        break

                                    if i == "1":
                                        low = i
                                    if i == "2":
                                        upp = i
                                    if i == "3":
                                        num = i
                                    if i == "4":
                                        sym = i

                                if not invalid:
                                    print("generated password")
                                    print(randomPassword(lng, low, upp, num, sym))

                            else:
                                print("Invalid selection")

                else:
                    print(f">> Inserted: {user} < invalid length.")

            else:
                print(f">> Inserted: {user} < invalid length.")

        else:
            print("Invalid choice, please try again.")