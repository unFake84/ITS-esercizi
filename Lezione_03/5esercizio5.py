# alien_color = ["Verde"]

n: str = (input("Di che colore è l'alieno?\nVerde, Giallo o Rosso?: "))

if n.title() == "Verde": # .TITLE serve per accettare qualsiasi grandezza nella parola N(utente)

    print("Hai guadagnato 5 punti!Per aver colpito l'alieno verde!")

elif n.title() == "Giallo":

    print("Hai guadagnato 10 punti!Per aver colpito l'alieno giallo!")

elif n.title() == "Rosso":

    print("Hai guadagnato 15 punti!Per aver colpito l'alieno rosso!")

else:

    print("banana")