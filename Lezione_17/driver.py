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

from dottore import Doctor
from paziente import Patient
from fatture import Bill
import random

d1: Doctor = Doctor("Lucio", "Sestio", "Cardiologo", 80.5)
d1.setAge(57)
d2: Doctor = Doctor("Numidio", "Quadraro", "Fisiatra", 77.8)
d2.setAge(49)

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

l_p1: list[Patient] = [p1, p2, p3, p4, p5]
for patient in l_p1:

    patient.setAge(random.randint(20, 70))

l_p2: list[Patient] = [p6, p7, p8, p9, p10]
for patient in l_p2:

    patient.setAge(random.randint(20, 70))

# lista_di_pazienti1: list[Patient] = []
# lista_di_pazienti2: list[Patient] = []

# for _ in range(3):

#     lista_di_pazienti1.append(random.choice(l_p1))

# print(lista_di_pazienti1)