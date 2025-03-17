'''
Changing Guest List:'
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