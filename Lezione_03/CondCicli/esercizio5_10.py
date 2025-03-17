# creo varie liste per fare vari test.
#current_users: list[str] = ["Alpha", "Beta", "Charlie", "Delta", "Echo"]
current_users: list[str] = ["alpha", "beta", "charlie", "delta", "echo"]
new_users: list[str] = ["Foxtrot", "Alpha", "Golf", "Echo", "India", "BETA", "deLTa"]

# UI che mostra le 2 liste CURRENT e USER.
print(".----------------------------------------------------------------------.")
print(f"|          [[{current_users}]]           |")
print(f"|  [[{new_users}]]  |")
print("'----------------------------------------------------------------------'")

# ciclo FOR per entrare nel loop.
for user in new_users:

    # .LOWER per convertire (l'input) l'elemento della lista 'new' in minuscolo
    # se 'user' iterando dentro la lista 'current' vede che è già nella lista
    if user.lower() in current_users:

        print(f"[{user}] username already been used, please change it.")

    # altrimenti
    else:

        print(f"[{user}] is avaiable. Please proceed.")