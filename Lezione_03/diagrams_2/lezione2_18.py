i: int = 1
somma: int = 0
media: int = 0
somma_pari: int = 0
somma_dispari: int = 0

while True:

    try:

        soglia: int = (int(input("Inserire una soglia: ")))

        if soglia > 0:

            while i <= soglia:
                    
                    try:

                        utente: int = (int(input(f"Inserire il {i}° numero di {soglia}: ")))

                        somma += utente
                        media = somma / i

                        if utente%2 == 0:                             
                             
                            somma_pari += utente

                        elif utente < media or utente%2 != 0:
                             
                            somma_dispari += utente

                        i += 1

                    except ValueError:
                         
                        print("Il valore inserito non è leggibile")

            break

        else:

            print("Il numero deve essere positivo.")

    except ValueError:

        print("Il valore inserito non è leggibile.")

print(somma_pari)
print(somma_dispari)

if somma_pari > somma_dispari:
     
    print("Somma pari è maggiore.")

else:

    print("Somma dispari è maggiore.")