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


def is_valid_ipv4(address: str) -> bool:

    checker: list[str] = address.split(".")

    if len(checker) != 4:
        return False

    for octet in checker:

        if not octet.isdigit():
            return False

        isint: int = int(octet)

        if isint < 0 or isint > 255:
                return False

    return True





def check_ipv4(ip: str) -> bool:
    ip = ip.split()
    if len(ip) != 4:
        return False # 4 punti
    for blocco in ip:
        if not blocco.isdigit():
            return False # carr alfabetico
        if not (0 <= int(blocco) <= 255):
            return False # !no 0<n<255
    return True




if __name__ == "__main__":

    print("Risultato atteso: True\nOttenuto: ", is_valid_ipv4("192.168.0.1"), "\n") # True
    print("Risultato atteso: True\nOttenuto: ", is_valid_ipv4("255.255.255.255"), "\n") # True
    print("Risultato atteso: False\nOttenuto: ", is_valid_ipv4("256.100.10.1"), "(256 è fuori range)", "\n") # False (256 è fuori range)
    print("Risultato atteso: False\nOttenuto: ", is_valid_ipv4("192.168.1"), "(solo 3 parti)", "\n") # False (solo 3 parti)
    print("Risultato atteso: False\nOttenuto: ", is_valid_ipv4("192.168.1.a\n"), "(parte non numerica)", "\n") # False (parte non numerica)


























    # check_len: int = len(address)
    # check_point: int = 0
    # char_isint: int = 0
    # pre_check: str = ""

    # if check_len > 15:
    #     return False

    # for char in address:

    #     if check_point > 3:
    #         return False

    #     if char == ".":

    #         check_point += 1

    #         try:
    #             char_isint = int(pre_check)
    #         except ValueError:
    #             return False

    #         pre_check = ""

    #         if char_isint < 0 or char_isint > 255:
    #             return False

    #     if char != ".":
    #         pre_check += char

    # try:
    #     char_isint = int(pre_check)
    # except ValueError:
    #     return False

    # if char_isint < 0 or char_isint > 255:
    #     return False

    # return True if check_point == 3 else False





# import string
# from string import ascii_lowercase, ascii_uppercase

# def is_valid_ipv4(address: str) -> bool:

#     # a_z_lower: str = ascii_lowercase
#     # a_z_upper: str = ascii_uppercase
#     # car_special: str = string.punctuation
#     check_len: int = len(address)
#     check_point: int = 0
#     char_isint: int = 0
#     pre_check: str = ""

#     if check_len > 15:
#         return False

#     for char in address:

#         if check_point > 3:
#             return False

#         if char == ".":

#             # if pre_check == "":
#             #     return False

#             check_point += 1

#             try:
#                 char_isint = int(pre_check)
#             except ValueError:
#                 return False

#             pre_check = ""

#             if char_isint < 0 or char_isint > 255:
#                 return False

#         # if char in a_z_lower or char in a_z_upper:
#         #     return False

#         # if char in car_special and char != ".":
#         #     return False

#         # # pre_check: int | str
#         # # pre_check = int(char) if char != '.' else "controlla"

#         if char != ".":
#             pre_check += char

#     try:
#         char_isint = int(pre_check)
#     except ValueError:
#         return False

#     if char_isint < 0 or char_isint > 255:
#         return False

#     return True if check_point == 3 else False


# def isdigit_valid_ipv4(address: str) -> bool:
#     points: int = 0
#     i_ottetto: str = ""
#     ii_ottetto: str = ""
#     iii_ottetto: str = ""
#     iv_ottetto: str = ""
#     for index in range(len(address)):
#         if address[index] == ".":
#             if points in (0,1,2,3):
#                 points += 1
#             else:
#                 False
#         elif address[index] != ".":
#             if points == 0:
#                 i_ottetto += address[index]
#             elif points == 1:
#                 ii_ottetto += address[index]
#             elif points == 2:
#                 iii_ottetto += address[index]
#             elif points == 3:
#                 iv_ottetto += address[index]
#     try:
#         i: int = int(i_ottetto)
#         ii: int = int(ii_ottetto)
#         iii: int = int(iii_ottetto)
#         iv: int = int(iv_ottetto)
#     except ValueError:
#         return False
    
#     return True
#         # print()
#         # print(i_ottetto, ii_ottetto, iii_ottetto, iv_ottetto)