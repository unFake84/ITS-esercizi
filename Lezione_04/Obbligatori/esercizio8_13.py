'''
User Profile:
Build a profile of yourself by calling build_profile(),
using your first and last names and three other key-value pairs that describe you.
All the values must be passed to the function as parameters.
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
'''

def build_profile(name: str, surname: str, age: int, hair: str, weight: int) -> str:

    return f"{name} {surname}, age {age}, hair {hair}, weight {weight}"

if __name__ == "__main__":

    profile: str = build_profile(name="Dioni", surname= "Manon", age=40, hair="brown", weight=85)

    print(profile)