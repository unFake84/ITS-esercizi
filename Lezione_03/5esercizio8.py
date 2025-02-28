usernames: list[str] = ["admin", "bob", "dylan", "tex", "kit"]
print("-----------------------------------------------------------------------")
print("Benvenuti\nInserire il proprio nome utente per accedere al sistema.")
print("-----------------------------------------------------------------------")

for user in usernames:
    
        if user == "admin":
        
            print("Hello admin, would you like to see a status report?")
            print("-----------------------------------------------------------------------")
            
        else:
            
            print(f"Hello {user}, thank you for logging in again.")
            print("-----------------------------------------------------------------------")