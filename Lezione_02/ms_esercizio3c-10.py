'''
Scrivere un programma in Python
che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica),
salvi la data in una tupla e utilizzi un match statement
per verificare se la data corrisponde a una festività o a un evento speciale
'''

import time
import os

print("\nBenvenuti\n")

while True:

    try:

        user_data: int = (int(input("Inserire giorno: ")))
        user_mese: int = (int(input("Inserire mese: ")))

        print("")

        if user_mese <= 0 or user_mese > 12:

            print("Per favore inserire una data valida.\n")
            continue

        elif user_mese == 2:

            if user_data < 1:
                
                print("Per favore inserire una data valida.\n")
                continue
                
            elif user_data > 29:

                print("Febbraio può avere massimo 29 giorni!\n")
                continue

        elif user_mese == 4 or user_mese == 6 or user_mese == 9 or user_mese == 11:

                if user_data < 1 or user_data > 30:

                    print("Questo mese arriva fino al 30!\n")
                    continue

        elif user_mese != 2:

            if user_data < 1 or user_data > 31:

                print("Per favore inserire una data valida.\n")
                continue
        
        break

    except ValueError:

        print("Per favore inserire una data valida.\n")

datamese: tuple[int, int] = (user_data, user_mese)

match datamese:

    case (1, 1):

        print(f"Il {datamese[0]}/{datamese[1]} è capodanno!\n")

    case(14, 2):

        print(f"Il {datamese[0]}/{datamese[1]} è San Valentino!\n")

    case(9, 3):

        print("E' il compleanno di Uccia!\n")

    case(2, 6):

        print(f"Il {datamese[0]}/{datamese[1]} è la festa della Repubblica Italiana!\n")

    case(15, 8):

        print(f"Il {datamese[0]}/{datamese[1]} è ferragosto!\n")

    case(31, 10):

        print(f"Il {datamese[0]}/{datamese[1]} è il mio compleanno!\n")

    case(25, 12):

        print(f"Il {datamese[0]}/{datamese[1]} è Natale!\n")

    case(31, 12):

        print(f"Il {datamese[0]}/{datamese[1]} è la fine dell'anno!\n")

    case _:

        print("Nessuna festività importante in questa data.\n")

while True:

        scelta: str = (input("Vuoi riavviare il programma?\n'si' per riavviare, 'no' per chiudere: "))

        if scelta.lower() == 'no':

            print("\nBuona giornata\n")
            time.sleep(2)
            os.system('clear')
            time.sleep(1)
            break

        elif scelta.lower() == 'si':

            print("\nRiavvio in corso\n")
            time.sleep(3)
            os.system('clear')
            os.system('/usr/bin/python3 /home/its/Esercizi/Lezione_02/ms_esercizio3c-10.py')
            break

        print("\nInserire 'si' o 'no'\n")