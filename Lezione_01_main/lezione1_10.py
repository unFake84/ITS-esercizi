r: int = int(input("inserisci il tuo reddito: "))
m: int = int(input("inserisci voto: "))

if r < 20000 and m > 27:

    print("Borsa di studio approvata")

else:
    
    print("Borsa di studio rifiutata, reddito o media insufficiente")
