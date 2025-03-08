'''
Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y)
e salvi le coordinate inserite in una tupla.
Utilizzare il match statement per determinare la sua posizione del punto inserito nel piano cartesiano
'''

while True:

    try:

        user_x: int = (int(input("Inserire coordinata X: ")))
        user_y: int = (int(input("Inserire coordinata Y: ")))
        break

    except ValueError:

        print("Per favore inserire una coordinata valida.")

coordinate: tuple[int, int] = (user_x, user_y)

match coordinate:

    
    case (0, 0):

        print(f"Il punto (0, 0) si trova nell'origine.")

    case (x, 0):

        print(f"Il punto ({x}, 0) si trova sull'asse X.")

    case (0, y):

        print(f"Il punto (0, {y}) si trova sull'asse Y.")

    case(x, y):

        if x > 0 and y > 0:

            print(f"Il punto ({x}, {y}) si trova nel primo quadrante.")

        elif x < 0 and y > 0:

            print(f"Il punto ({x}, {y}) si trova nel secondo quadrante.")

        elif x < 0 and y < 0:

            print(f"Il punto ({x}, {y}) si trova nel terzo quadrante.")

        else:

            print(f"Il punto {x, y} si trova nel quarto quadrante.") # si puo fare anche così, mostra le parentesi della tupla