'''
### Codice Driver

Scrivere, infine, il codice driver che gestisca due dottori e due liste di pazienti.
La prima lista di pazienti deve contenere 3 pazienti, mentre la seconda 1 solo paziente.

    Impostare l'età di ogni medico, affinché i due medici risultino validi!
    Il primo medico e il secondo medico si presentano, richiamando il rispettivo metodo doctorGreet().
    Creare un oggetto fattura chiamato fattura1.
    Alla fattura 1 devono essere associati il dottore_1 e la lista di 3 pazienti.
    Creare un oggetto fattura chiamato fattura2.
    Alla fattura 2 devono essere associati il dottore_2 e la lista di un solo paziente.
    Stampare in output il salario di ogni singolo dottore. Ad esempio:

      "Salario Dottore1: ... euro!
       Salario Dottore2: ... euro!"

    Rimuovere un paziente dalla lista dei pazienti del dottore 1
    ed inserire tale paziente nella lista del dottore 2.
    Stampare in output il salario di ogni dottore.
    Stampare in output il guadagno totale incassato dall'ospedale.
    Il guadagno totale viene calcolato sommando i guadagni di ogni dottore. Esempio:

"In totale, l'ospedale ha incassato: tot euro!"
'''

# importo le classi + modulo random per rendere randomico lo smistamento dei pazienti
from dottore import Doctor
from paziente import Patient
from fatture import Bill
import random

# creo 2 dottori validi assegnandoli l'età giusta
dottore_1: Doctor = Doctor("Lucio", "Sestio", "Cardiologo", 80.5)
dottore_1.setAge(57)
dottore_2: Doctor = Doctor("Numidio", "Quadraro", "Fisiatra", 77.8)
dottore_2.setAge(49)

# non avevo letto il limite di 4 pazienti totali
p1: Patient = Patient("Lucia", "Gialli", "001")
p2: Patient = Patient("Luca", "Verdi", "002")
p3: Patient = Patient("Andrea", "Marroni", "003")
p4: Patient = Patient("Marco", "Rossi", "004")
p5: Patient = Patient("Davide", "Blu", "005")
p6: Patient = Patient("Lorenzo", "Magenta", "006")
p7: Patient = Patient("Simone", "Bianchi", "007")
p8: Patient = Patient("Anna", "Arancioni", "008")
p9: Patient = Patient("Giada", "Neri", "009")
p10: Patient = Patient("Giulia", "Viola", "010")

# quindi, decido di creare, una lista di 5 pazienti (invece di 3)
l_p1: list[Patient] = [p1, p2, p3, p4, p5]

# e di assegnare a ciascuno di loro un'età random da 10 a 99
for patient in l_p1:

    patient.setAge(random.randint(10, 99))

# e un altra lista di 5 pazienti (invece di 1)
l_p2: list[Patient] = [p6, p7, p8, p9, p10]

for patient in l_p2:

    patient.setAge(random.randint(10, 99))

# visto che ormai avevo creato 10 pazienti, ho deciso di assegnarli in modo casuale.
# prima, ho creato una lista di pazienti da essere assegnati, unendo le due precedenti liste
pazienti_da_assegnare: list[Patient] = l_p1 + l_p2
# utilizzo shuffle per mescolare in modo random la lista dei pazienti da assegnare
random.shuffle(pazienti_da_assegnare)

lista_pazienti_uno: list[Patient] = pazienti_da_assegnare[:3]   # i primi 3 elementi della lista
lista_pazienti_due: list[Patient] = [pazienti_da_assegnare[3]]  # 4 elemento della lista

# presento i dottori
dottore_1.doctorGreet()
print("")
dottore_2.doctorGreet()

print("")

# creo due oggetti fattura, assegnando le due liste di pazienti ed i rispettivi dottori
fattura1: Bill = Bill(lista_pazienti_uno, dottore_1)
fattura2: Bill = Bill(lista_pazienti_due, dottore_2)

print("")

# mostro il fatturato
print(f"Salario Dottore1: {fattura1.getSalary():.2f} euro!")
print(f"Salario Dottore2: {fattura2.getSalary():.2f} euro!")

print("")

# sempre in modo random, vado a prendere l'index e
# creo una copia del paziente che verrà spostato
numero_random = random.randint(0, 2)
paziente_da_spostare: Patient = lista_pazienti_uno[numero_random]

fattura1.removePatient(paziente_da_spostare.getIdCode())    # qui il prescelto verrà rimosso dalla parcella del dottore1,
fattura2.addPatient(paziente_da_spostare)                   # per essere assegnato alla parcella del dottore2

print("")

# mostro il fatturato aggiornato
print(f"Salario Dottore1: {fattura1.getSalary():.2f} euro!")
print(f"Salario Dottore2: {fattura2.getSalary():.2f} euro!")

# sommo le due fatture per mostrare il totale fatturato
totale: float = fattura1.getSalary() + fattura2.getSalary()

print("")
print(f"In totale, l'ospedale ha incassato: {totale:.2f} euro!")




























# questa variabile len evita di andare fuori range quando i pazienti verranno assegnati ai rispettivi dottori
# len_lista_pazienti_da_assegnare: int = len(pazienti_da_assegnare) - 1
# for paziente in pazienti_da_assegnare:

#     # la lista1 può avere massimo 3 slots
#     if len(lista_pazienti_uno) <= 2:
#         # qui creo un numero random da 0 a 9 <- len_listaetc scende ad ogni iterazione, evitando così index out of range
#         numero_random: int = random.randint(0, len_lista_pazienti_da_assegnare)
#         lista_pazienti_uno.append(pazienti_da_assegnare[numero_random]) # assegno un paziente disponibile alla lista1
#         pazienti_da_assegnare.pop(numero_random) # rimuovo il paziente dalla lista di assegnazione
#         len_lista_pazienti_da_assegnare -= 1 # ogni volta che un paziente viene assegnato, bisogna ridurre la lista di assegnazione

#     # stessa cosa ma con un solo slot disponibile
#     if len(lista_pazienti_due) <= 0:
#         numero_random = random.randint(0, len_lista_pazienti_da_assegnare)
#         lista_pazienti_due.append(pazienti_da_assegnare[numero_random])
#         pazienti_da_assegnare.pop(numero_random)
#         len_lista_pazienti_da_assegnare -= 1