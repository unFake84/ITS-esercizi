# alien_color = ["Verde"]

n: str = (input("Di che colore è l'alieno?\nVerde, Giallo o Rosso?: "))

if n.title() == "Verde": # .TITLE serve per accettare qualsiasi grandezza nella parola N(utente)

    print("Hai guadagnato 5 punti!")