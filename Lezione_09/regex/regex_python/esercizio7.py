'''

Verifica un nome proprio

Scrivi una funzione is_valid_name(name) che controlla
se la stringa inizia con una lettera maiuscola seguita da almeno due lettere minuscole.

Esempio:

is_valid_name("Marco")    # True
is_valid_name("marco")    # False
is_valid_name("Ma")       # False

'''

import re

def is_valid_name(name: str) -> bool:

    if re.fullmatch(r'[A-Z][a-z]{2,}', name) == None:

        return False
    
    else:

        return True

if __name__ == "__main__":

    print(is_valid_name("Marco"))
    print(is_valid_name("marco"))
    print(is_valid_name("Ma"))