usernames: list[str] = ["admin", "bob", "dylan", "tex", "kit"]
# usernames: list[str] = []
print("-----------------------------------------------------------------------")
print("Benvenuti\nInserire il proprio nome utente per accedere al sistema.")

if usernames == []:
         
        print("We need to find some users!")

print("-----------------------------------------------------------------------")

for user in usernames:
    
        if user == "admin":
        
            print("Hello admin, would you like to see a status report?")
            print("-----------------------------------------------------------------------")
            
        if user in usernames and user != "admin":
            
            print(f"Hello {user}, thank you for logging in again.")
            print("-----------------------------------------------------------------------")

while usernames:
      
        usernames.pop()

# # secondo metodo
# usernames.clear()

# # terzo metodo
# usernames: list[str] = []

# # quarto metodo
#del(usernames)

print(f"{usernames} List deleted!")
print("-----------------------------------------------------------------------")

# # teoricamente..
# if usernames == []:
         
        # print("We need to find some users!")