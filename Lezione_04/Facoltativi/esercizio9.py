'''
Caesar Cipher Encryption/Decryption

    Create functions for encrypting and decrypting a message using the Caesar cipher.
    Allow the user to specify the shift value (number of positions to shift each letter).
    Handle both encryption and decryption using the same function with appropriate adjustments.
    Encrypt and decrypt the given message using the specified shift value.

'''

from string import ascii_lowercase, ascii_uppercase

def enOrDecrypt(text: str, key: int, decr: bool = None) -> str:

    chars: list[str] = list(text.strip())
    en_de_crypted: str = ""

    for char in chars:

        if char in ascii_lowercase or char in ascii_uppercase:
            for i2, l2 in enumerate(ascii_lowercase):

                if char == l2 or char == ascii_uppercase[i2]:

                    en_de_crypted += ascii_lowercase[(i2 + key)%26 if decr is None else (i2 - key)%26]\
                        if char in ascii_lowercase else\
                            ascii_uppercase[(i2 + key)%26 if decr is None else (i2 - key)%26]

        else:
            en_de_crypted += char

    return en_de_crypted

if __name__ == "__main__":

    print(enOrDecrypt("aBcd! aZ", 1))
    print(enOrDecrypt("bCde! bA", 1, True))