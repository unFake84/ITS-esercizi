# creo una funzione(ricorsiva) che, richiama se stessa + volte per effettuare operazioni
def recursivePower(a: int, b: int) -> int:

    # se uno dei numeri è negativo, stampa un messaggio di errore
    if a < 0 or b < 0:

        print("Errore i numeri sono negativi")
        
        # restituisce None per chiarire che l'operazione non è stata eseguita
        return None

    # se la potenza è 0, ritorna 1 perché qualsiasi numero elevato alla potenza 0 è 1
    elif b == 0:

        return 1

    # se entrambi i numeri sono positivi, moltiplica a per il risultato della funzione ricorsiva con b-1
    else:

        return a * recursivePower(a, b - 1)

if __name__ == "__main__":

    print(f"3 elevato alla 4 = {recursivePower(3, 4)}")