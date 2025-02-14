num_NS: int = int(input("inserire automobili da Nord a Sud: "))
num_EO: int = int(input("inserire automobili da Est o Ovest: "))
soglia: int = int(input("inserire soglia max!: "))
tempo_priorità: int = int(input("inserire la priorità del tempo!: "))

if num_NS > soglia:

    if num_EO > soglia:
        tempo_NS = 50
        tempo_EO = 50

    else:
        tempo_NS = tempo_priorità
        tempo_EO = 100-tempo_priorità


elif num_EO > soglia:
    tempo_NS = 100-tempo_priorità

else:
    veicoli_tot = num_NS+num_EO
    tempo_NS = num_NS/veicoli_tot*100
    tempo_EO = 100-tempo_NS

print(f"{tempo_EO}%")
print(f"{tempo_NS}%")