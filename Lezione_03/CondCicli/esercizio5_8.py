# creo lista
usernames: list[str] = ["admin", "bob", "dylan", "tex", "kit"]

# piccola interfaccia :)
print("-----------------------------------------------------------------------")
print("Benvenuti\nInserire il proprio nome utente per accedere al sistema.")
print("-----------------------------------------------------------------------")

# utilizzo ciclo FOR per iterare la lista con USER che se:
for user in usernames:
    
        # ad ogni iterazione USER è simile '==' alla parola admin:
        if user == "admin":
        
            # accesso privilegiato
            print("Hello admin, would you like to see a status report?")
            print("-----------------------------------------------------------------------")
            
        # altrimenti ELSE, accesso utente.
        else:
            
            print(f"Hello {user}, thank you for logging in again.")
            print("-----------------------------------------------------------------------")