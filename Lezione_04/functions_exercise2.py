'''
Exercise 2
Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.
'''

def check_lenght(stringa: str):

    if len(stringa) == 10:
        
        print(f"La frase [{stringa}] ha esattamente 10 caratteri")

    elif len(stringa) > 10:

        print(f"La frase [{stringa}] ha più di 10 caratteri")

    else:

        print(f"La frase [{stringa}] ha meno di 10 caratteri")

check_lenght(input("Inserire una frase,\nper determinare se i caratteri totali sono,\nmaggiori o uguali a 10\nspazi compresi: "))