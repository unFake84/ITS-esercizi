i: int = 1
somma: int = 0
media: int = 0
t_max: int = 0
t_min: int = 0
day_max:int = 0
day_min:int = 0
count_norma:int = 0

print("-----------------------------------------------------------------------")

while i <= 7:

    try:

        user: float = (float(input(f"Inserire {i}° temperatura: ")))

        somma += user
        media += 1

        if user >= 10 and user <= 30:

            count_norma += 1

        elif user > 35 or user < 5:

            print("Allerta temperatura!")

        if i == 1:

            t_max = user            
            t_min = user

        if user >= t_max:

            t_max = user
            day_max = i

        elif user <= t_min:

            t_min = user
            day_min = i

        i += 1
        print("-----------------------------------------------------------------------")

    except ValueError:

        print("Inserire una numerazione valida.")

'''
print(count_norma) # senza di questo non funziona il rigo '59': IF COUNT_NORMA == 7: verificare.
'''

media = somma/7

print(f"La media delle temperature è: {media:.2f}")

if count_norma == 7:

    print("Temperature nella norma")

if day_max > -1 and day_max < 1:

    day_max == 1

print(f"Il {day_max}° giorno della settimana era la più calda!")
print(f"Il {day_min}° giorno della settimana era la più fredda!")
print("-----------------------------------------------------------------------")