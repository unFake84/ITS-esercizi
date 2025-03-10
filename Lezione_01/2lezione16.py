dispari: int = 0
pari: int = 0
negativi: int = 0
positivi: int = 0
i: int = 1

while i <= 10:

    try:

        user: int = (int(input(f"[{i}/10]: Inserire il {i}° numero: ")))

        if user != 0:

            if user > 0:

                positivi += 1

                if user%2 == 0 and user >= 20:

                    pari += 1

            else:
                
                negativi += 1

                if user%2 == 0 and user <= -10:

                    dispari += 1

    except ValueError:

        print("Non è stato inserito un numero intero.")
        i -= 1
    
    i += 1

print(f"I numeri positivi sono: {positivi}")
print(f"I numeri negativi sono: {negativi}")
print(f"I numeri positivi pari e maggiori di 20 sono: {pari}")
print(f"I numeri negativi pari e minori di 10 sono: {dispari}")