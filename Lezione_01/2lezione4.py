n_tutor = 10
attesa = 0

print(f"Il numero dei tutor attuali è: {n_tutor}!")

while n_tutor > 0 or attesa < 50: # il repeat in Python non esiste: bisogna trasformarlo in while e posizionarlo in alto, non in basso

    studente: str = str(input("Inserire nome studente: "))
    
    if n_tutor > 0:

        print("Tutor assegnato con successo!")
        n_tutor -= 1

    else:
        print("Studente in attesa")
        attesa += 1

print(f"Il numero dei tutor attuali è: {n_tutor}")