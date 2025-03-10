user_variabili: int = (int(input("\nInserire un numero di operazioni da effettuare: ")))

i: int = 1

while i <= user_variabili:

    print(f"\n[Operazione {i} di {user_variabili}]")

    user_x: int = (int(input("Inserire il valore di 'X': ")))
    user_y: int = (int(input("Inserire il valore di 'Y': ")))

    if user_x > 0 and user_y > 0:

        print(f"Il prodotto tra {user_x} e {user_y} è: {user_x * user_y}.\n")

    elif user_x > 0 and user_y < 0 or user_x < 0 and user_y > 0:

        print(f"La somma tra {user_x} e {user_y} è: {user_x + user_y}.\n")
        
    else:

        print(f"\nErrore, hai inserito {user_x} e {user_y}!\n")
        i -= 1

    i += 1

print(f"Terminato, hai {user_variabili - user_variabili} operazioni disponibili.")