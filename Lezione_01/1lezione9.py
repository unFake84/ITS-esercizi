nome: str = str(input("inserisci un nome: "))
vendite: int = int(input("inserisci una vendita: "))
max_nome = nome
max = 0
min_nome = nome
min = 1000000000
cont = 0

while cont < 3:

    new_nome: str = str(input("Inserire nuovo nome: "))
    new_vendite: int = int(input("Inserire nuova vendita: "))

    if new_vendite > max:

        max_nome = new_nome
        max = new_vendite

    else:
        
        if new_vendite < min:
            min_nome = new_nome
            min = new_vendite

    cont += 1

print(f"{max_nome=} {max=} {min_nome=} {min=}")