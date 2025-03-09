'''
Scrivere un programma in Python
che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica),
salvi la data in una tupla e utilizzi un match statement
per verificare se la data corrisponde a una festività o a un evento speciale
'''

import time
import os

print("Benvenuti")

while True:

    try:

        user_data: int = (int(input("Inserire giorno: ")))
        user_mese: int = (int(input("Inserire mese: ")))

        if user_mese <= 0 or user_mese > 12:

            print("Per favore inserire una data valida.")
            continue

        elif user_mese == 2:

            if user_data < 1:
                
                print("Per favore inserire una data valida.")
                continue
                
            elif user_data > 29:

                print("Febbraio può avere massimo 29 giorni!")
                continue

        elif user_mese != 2:

            if user_data < 1 or user_data > 31:

                print("Per favore inserire una data valida.")
                continue
        
        break

    except ValueError:

        print("Per favore inserire una data valida.")

datamese: tuple[int, int] = (user_data, user_mese)

match datamese:

    case (1, 1):

        print(f"Il {datamese[0]}/{datamese[1]} è capodanno!")

    case(14, 2):

        print(f"Il {datamese[0]}/{datamese[1]} è San Valentino!")

    case(9, 3):

        print("E' il compleanno di Uccia!")

    case(2, 6):

        print(f"Il {datamese[0]}/{datamese[1]} è la festa della Repubblica Italiana!")

    case(15, 8):

        print(f"Il {datamese[0]}/{datamese[1]} è ferragosto!")

    case(31, 10):

        print(f"Il {datamese[0]}/{datamese[1]} è il mio compleanno!")

    case(25, 12):

        print(f"Il {datamese[0]}/{datamese[1]} è Natale!")

    case(31, 12):

        print(f"Il {datamese[0]}/{datamese[1]} è la fine dell'anno!")

    case _:

        print("Nessuna festività importante in questa data.")

scelta: str = (input("Vuoi riavviare il programma?\n'si' per riavviare 'no' per chiudere: "))

while True:

    match scelta:

        case scelta if scelta == 'si':

            print("Riavvio in corso")
            time.sleep(3)
            os.system('/usr/bin/python3 /home/its/Esercizi/Lezione_02/ms_esercizio3c-10.py')
            time.sleep(1)
            break

        case scelta if scelta == 'no':

            print("Buona giornata")
            time.sleep(2)
            os.system('clear')
            time.sleep(1)
            break

        case _:

            print("Inserire 'si o 'no'.\n")
            continue