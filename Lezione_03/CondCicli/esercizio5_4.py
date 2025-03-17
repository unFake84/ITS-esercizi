# rispettando la traccia
# alien_color = ["Verde"]

# sempre piu dinamico
n: str = (input("Di che colore è l'alieno?\nVerde, Giallo o Rosso?: "))

# .TITLE serve per trasformare qualsiasi input inserito con la prima in maiuscolo ':...'
# se la parola inserita 'N' è '==' a 'Verde' ^
if n.title() == "Verde":

    # entra nell'istruzione e printa 5 punti
    print("Hai guadagnato 5 punti!Per aver sparato all'alieno verde!")

else:

    # non dovrebbe funzionare così.. ma è così.
    print("Hai guadagnato 10 punti!Per aver colpito niente!")