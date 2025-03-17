# creo lista di utenti già registrati
usernames: list[str] = ["admin", "bob", "dylan", "tex", "kit"]

#,,,
# usernames: list[str] = []
#'''

# umb + user interface(o similar)
print("-----------------------------------------------------------------------")
print("Benvenuti\nInserire il proprio nome utente per accedere al sistema.")

# CLONE 1
# seguendo i punti della traccia, questa condizione viene posizionata qui.
# ovvero se la lista è vuota/mancano utenti.
if usernames == []:
         
        print("We need to find some users!")

print("-----------------------------------------------------------------------")

# ciclo FOR per cominciare il loop
for user in usernames:
    
        # se admin
        if user == "admin":
        
            print("Hello admin, would you like to see a status report?")
            print("-----------------------------------------------------------------------")
            
        # altrimenti
        else:
            
            print(f"Hello {user}, thank you for logging in again.")
            print("-----------------------------------------------------------------------")

# con ciclo WHILE entro per rimuovere gli elementi con la 'funzione' .POP [I METODO]
while usernames:
      
        usernames.pop()

# # [II METODO]
# usernames.clear()

# # [III METODO]
# usernames: list[str] = []

# # [IV METODO]
#del(usernames)

print(f"{usernames} List deleted!")
print("-----------------------------------------------------------------------")

# CLONE 2
# # teoricamente..non seguendo la traccia.
# if usernames == []:
         
        # print("We need to find some users!")