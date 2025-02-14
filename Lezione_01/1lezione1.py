import math

A = int(input("Inserire l'Ipotenusa: "))
B = int(input("Inserire un Cateto: "))
if A > B:
    C = math.sqrt(A**2-B**2)
    print(f"L'altro cateto è: {C}")
else:
    print("Errore dati non validi")