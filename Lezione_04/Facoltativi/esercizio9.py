'''
Caesar Cipher Encryption/Decryption

    Create functions for encrypting and decrypting a message using the Caesar cipher.
    Allow the user to specify the shift value (number of positions to shift each letter).
    Handle both encryption and decryption using the same function with appropriate adjustments.
    Encrypt and decrypt the given message using the specified shift value.

'''

from string import ascii_lowercase

def encrypt(text: str, key: int) -> str:
    text: list[str] = list(text.strip())
    print(text)

    for i, l in enumerate(ascii_lowercase):

        pass

if __name__ == "__main__":
    encrypt("abcd", 4)