'''
Shrinking Guest List:
'''

import time

dinner: list = ["Chopin", "Mozart", "Bach"]

for i in dinner:
    
    print(f"Il Sig. {i}, è invitato a cena!")
    time.sleep(1)

print("Il Sig. Bach ha dovuto disdire la cena!")
time.sleep(1)

print("Nuova lista di invitati")
time.sleep(1)

dinner.pop(2)
dinner.append("Beethoven")

for i in dinner:
    
    print(f"Il Sig. {i}, è invitato a cena!")
    time.sleep(1)

print("E' stato trovato un tavolo con altri posti!")
time.sleep(1)

dinner.insert(0, "Schubert")
dinner.insert(2, "Debussy")
dinner.insert(5, "Lizst")

for i in dinner:
    
    print(f"Il Sig. {i}, è invitato a cena!")
    time.sleep(1)
    
print(f"La lista degli invitati finali è: {dinner} ")
time.sleep(1)

print("Communicazione in arrivo.. ..Tavoli in ritardo..")
time.sleep(1)

print("E' necessario disdire gli invitati dalla cena fino ad un massimo di 2 posti!")
time.sleep(1)

dinner.pop(5)
print("Sig. Lizst siamo spiacenti di informarla che la cena è stata annullata.")
time.sleep(1)

dinner.pop(4)
print("Sig. Beethoven siamo spiacenti di informarla che la cena è stata annullata.")
time.sleep(1)

dinner.pop(3)
print("Sig. Mozart siamo spiacenti di informarla che la cena è stata annullata.")
time.sleep(1)

dinner.pop(2)
print("Sig. Debussy siamo spiacenti di informarla che la cena è stata annullata")
time.sleep(1)

print(f"La nuova lista degli invitati finali è: {dinner}")
time.sleep(1)

for i in dinner:

    print(f"Il sig. {i} è ancora invitato a cena")
    time.sleep(1)
    
del dinner[1]
del dinner[0]

# del dinner # soluzione sbagliata
# dinner = []

time.sleep(1)
print(f"{dinner} La lista è vuota")