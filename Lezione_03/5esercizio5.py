# rispettando la traccia
# alien_color = ["Verde"]

# ancora più dinamico!
n: str = (input("Di che colore è l'alieno?\nVerde, Giallo o Rosso?: "))

# prima condizione
if n.title() == "Verde": # .TITLE serve per accettare qualsiasi grandezza nella parola N(utente)

    # se VERA
    print("Hai guadagnato 5 punti!Per aver colpito l'alieno verde!")

# seconda condizione
elif n.title() == "Giallo":

    # se sì
    print("Hai guadagnato 10 punti!Per aver colpito l'alieno giallo!")

# terza condizione
elif n.title() == "Rosso":

    print("Hai guadagnato 15 punti!Per aver colpito l'alieno rosso!")

# altrimenti.
else:

    print("banana")