# creo lista
favorite_fruits: list[str] = ["Clementina", "Mandarino", "Banana"]



#------------------------------------------------------------------
# n: str = (input("Qual'è il mio frutto preferito?: ")).title()

# if n in favorite_fruits:
    
#     print(f"I really like: {n}")

# l'esercizio è funzionale anche da qui
# ma rispettando la traccia..::
#------------------------------------------------------------------



# 1 condizione
if "Clementina" in favorite_fruits:

    print("I really like Clementina!")

# 2 condizione
if "Mandarino" in favorite_fruits:

    print("After the Clementine I love Mandarins (if not sour)!")

# 3 condizione
if "Banana" in favorite_fruits:

    print("And finally the Banana is my third favourite fruit!")

# utilizzo il NOT IN esclusivamente per fare mostrare gli elementi fuori lista
if "Pineapple" not in favorite_fruits:

    print("Pineapple is good, but only occasionally!")

if "Grafruit" not in favorite_fruits:

    print("Grapeful is only good when squeezed")



#------------------------------------------------------------------
# uso ciclo FOR per trovare il frutto (serve INPUT!{n})
# for i in favorite_fruits:

#     if n == i:

#         print(f"I really like: {n}")
#------------------------------------------------------------------