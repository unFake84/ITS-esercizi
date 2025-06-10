'''
Validazione di un Indirizzo IPv4
Scrivi una funzione is_valid_ipv4(address: str) -> bool che determina se una
stringa è un indirizzo IPv4 valido. Un indirizzo IPv4 è composto da quattro numeri decimali
(ciascuno da 0 a 255) separati da punti (.). Gli zeri iniziali sono consentiti (ad esempio
192.168.001.001 è valido), ma ciascuna delle quattro parti deve essere compresa tra 0 e
255 e non deve contenere caratteri o spazi aggiuntivi.

                Requisiti:

● Se non ci sono esattamente tre punti o non ci sono quattro parti numeriche,
restituisci False.
● Ciascuna parte deve contenere solo cifre (isdigit()) e, convertita in intero, deve
essere nel range [0,255][0,255][0,255].


Esempi:
is_valid_ipv4("192.168.0.1") # True
is_valid_ipv4("255.255.255.255") # True
is_valid_ipv4("256.100.10.1") # False (256 è fuori range)
is_valid_ipv4("192.168.1") # False (solo 3 parti)
is_valid_ipv4("192.168.1.a") # False (parte non numerica)
'''

import string
from string import ascii_lowercase, ascii_uppercase

def is_valid_ipv4(address: str) -> bool:

    a_z_lower: str = ascii_lowercase
    a_z_upper: str = ascii_uppercase
    car_special: str = string.punctuation
    check_len: int = len(address)
    check_point: int = 0
    char_isint: int = 0
    pre_check: str = ""

    if check_len > 15:
        return False

    for char in address:

        if check_point > 3:
            return False

        if char == ".":

            if pre_check == "":
                return False

            check_point += 1
            char_isint = int(pre_check)
            pre_check = ""

            if char_isint < 0 or char_isint > 255:
                return False

        if char in a_z_lower or char in a_z_upper:
            return False

        if char in car_special and char != ".":
            return False

        # pre_check: int | str
        # pre_check = int(char) if char != '.' else "controlla"

        if char != ".":
            pre_check += char

    char_isint = int(pre_check)
    if char_isint < 0 or char_isint > 255:
        return False

    return True if check_point == 3 else False

if __name__ == "__main__":

    print("Risultato atteso: True\nOttenuto: ", is_valid_ipv4("192.168.0.1"), "\n") # True
    print("Risultato atteso: True\nOttenuto: ", is_valid_ipv4("255.255.255.255"), "\n") # True
    print("Risultato atteso: False\nOttenuto: ", is_valid_ipv4("256.100.10.1"), "(256 è fuori range)", "\n") # False (256 è fuori range)
    print("Risultato atteso: False\nOttenuto: ", is_valid_ipv4("192.168.1"), "(solo 3 parti)", "\n") # False (solo 3 parti)
    print("Risultato atteso: False\nOttenuto: ", is_valid_ipv4("192.168.1.a"), "(parte non numerica)", "\n") # False (parte non numerica)