# creo dizionario con stringhe ed interi
fav_numbers: dict[str, int] = {"A": 10, "B": 20, "C": 30, "D": 40, "E": 50}

# posso anche utilizzare il ciclo FOR con 2 iterabili e la funzione .ITEMS
# per prendere la lunghezza del dizionario usando
# key'chiave' e value'valore' ad ogni iterazione
for key, value in fav_numbers.items():

    # formattazione + key&value che si aggiornano ad ogni iterazione
    print(f"The alphabet {key}, like number {value}.")