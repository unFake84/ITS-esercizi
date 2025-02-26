# alien_color = ["Verde"]

n: str = (input("Di che colore è l'alieno?\nVerde, Giallo o Rosso?: "))

if n.title() == "Verde": # .TITLE serve per accettare qualsiasi grandezza nella parola N(utente)

    print("Hai guadagnato 5 punti!Per aver sparato all'alieno verde!")

else:

    print("Hai guadagnato 10 punti!Per aver colpito niente!")