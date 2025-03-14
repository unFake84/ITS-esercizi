'''
City Names:
Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this: "Santiago, Chile".
Call your function with at least three city-country pairs,
and print the values that are returned.
'''

def city_country(name: str, country: str) -> None:

    return f"{name.title()}, {country.title()}"

if __name__ == "__main__":

    print(city_country("salisburgo", "austria"))
    print(city_country("vienna", "austria"))
    print(city_country("london", "england"))