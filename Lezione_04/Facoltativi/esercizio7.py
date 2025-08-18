'''
Roman Numeral Conversion:

    Create a function that converts a given integer to its Roman numeral representation.
    Handle numbers from 1 to 3999.
    Use a combination of string manipulation and conditional statements to build the Roman numeral.

'''

def romanNumeralConversion(n: int) -> str:
    '''
    Handle numbers from 1 to 3999.
    '''

    if n >= 1 and n <= 3999:
        roman_tables: dict[str, int] = {
            "m": 1000,
            "cm": 900,
            "d": 500,
            "cd": 400,
            "c": 100,
            "xc": 90,
            "l": 50,
            "xl": 40,
            "x": 10,
            "ix": 9,
            "v": 5,
            "iv": 4,
            "i": 1
        }
        final_string: str = ""

        for roman, arabic in roman_tables.items():

            if n >= arabic:
                while n >= arabic:

                    final_string += roman
                    n -= arabic

    else:
        raise ValueError("Enter a number between 1 and 3999.")

    return final_string.upper()

if __name__ == "__main__":

    print(romanNumeralConversion(1984))

# i     > 1
# iv    > 4
# v     > 5
# ix    > 9
# x     > 10
# xl    > 40
# l     > 50
# xc    > 90
# c     > 100
# cd    > 400
# d     > 500
# cm    > 900
# m     > 1000