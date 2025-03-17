'''
Cars:
Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name.
It should then accept an arbitrary number of keyword arguments.
Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was stored correctly.
'''

def make_car(mark: str, model: str, **kwargs) -> dict:

    dictionary: dict = {}
    dictionary['mark'] = mark
    dictionary['model'] = model

    for key, value in kwargs.items():

            dictionary[key] = value

    return dictionary


if __name__ == "__main__":
      
        print(make_car("Mercedes", "Smart", year= 2010, tow_package= False, color= "white and grey"))