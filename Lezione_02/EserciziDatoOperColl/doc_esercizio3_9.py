'''
Dinner Guests:
'''

# names: list = ["a", "b", "c", "d", "e"]
# print(len(names))

import time

dinner: list = ["Chopin", "Mozart", "Bach"]

for i in dinner:
    
    print(f" Sig. {i}, è invitato a cena!")
    time.sleep(1)

print(f"{len(dinner)} persone sono state ivitate a cena")