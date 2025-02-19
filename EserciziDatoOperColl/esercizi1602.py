
# # 2-3: Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
# nome: str = "Dioni"
# print(f"Ciao {nome}, ti piacerebbe imparare un po' di Python oggi?")


# # 2-4: Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
# nome: str = "Dioni"
# lowercase = nome.lower()
# uppercase = nome.upper()
# title = nome.title()
# print(f"{lowercase}, {uppercase}, {title}")


# # 2-5: Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
# # 2-6: Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message
# autore: str = "Kit carson"
# cit: str = "Mai fasciarsi la testa prima di essersela rotta"
# print(f'{autore} una volta disse :"{cit}"') # le apici vanno in conflitto tra di loro se uguali, usare \"##\" per forzare le virgolette


# # 3-1: Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time
# names: list = ["a", "b", "c", "d", "e"]
# for name in names:
#     print(name)
   

# # 3-2: Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name
# names: list = ["a", "b", "c", "d", "e"]
# for name in names:
#     print(f"{name}, no f")
   

# # 3-3: Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
# moto: list = ["Ducati", "Yamaha", "Honda"]


# for i in range(len(moto)):
#     print(f"La {moto[i]}, è la mia {i+1}° preferita")

## print(f"La mia moto preferita in assoluto è, {moto[0]}")
## print(f"La mia seconda moto preferita è, {moto[1]}")
## print(f"La mia terza moto preferita è, {moto[2]}")


# # 3-4: Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner
# dinner: list = ["Chopin", "Mozart", "Bach"]

# for i in dinner:
#     print(f" Sig. {i}, è invitato a cena!")
    

# # 3-5: Changing Guest List:
# import time

# dinner: list = ["Chopin", "Mozart", "Bach"]

# for i in dinner:
    
#     print(f"Il Sig. {i}, è invitato a cena!")
#     time.sleep(1)

# print("Il Sig. Bach ha dovuto disdire la cena!")
# time.sleep(1)
# print("Nuova lista di invitati")
# time.sleep(1)
# dinner.pop(2)
# dinner.append("Beethoven")

# for i in dinner:
    
#     print(f"Il Sig. {i}, è invitato a cena!")
#     time.sleep(1)


# # 3-6: More Guests:
# import time

# dinner: list = ["Chopin", "Mozart", "Bach"]

# for i in dinner:
    
#     print(f"Il Sig. {i}, è invitato a cena!")
#     time.sleep(1)

# print("Il Sig. Bach ha dovuto disdire la cena!")
# time.sleep(1)
# print("Nuova lista di invitati")
# time.sleep(1)
# dinner.pop(2)
# dinner.append("Beethoven")

# for i in dinner:
    
#     print(f"Il Sig. {i}, è invitato a cena!")
#     time.sleep(1)

# print("E' stato trovato un tavolo con altri posti!")
# time.sleep(1)
# dinner.insert(0, "Schubert")
# dinner.insert(2, "Debussy")
# dinner.insert(5, "Lizst")

# for i in dinner:
    
#     print(f"Il Sig. {i}, è invitato a cena!")
#     time.sleep(1)
    
# print(f"La lista degli invitati finali è: {dinner} ")

# # 3-7: Shrinking Guest List:
# import time

# dinner: list = ["Chopin", "Mozart", "Bach"]

# for i in dinner:
    
#     print(f"Il Sig. {i}, è invitato a cena!")
#     time.sleep(1)

# print("Il Sig. Bach ha dovuto disdire la cena!")
# time.sleep(1)
# print("Nuova lista di invitati")
# time.sleep(1)
# dinner.pop(2)
# dinner.append("Beethoven")

# for i in dinner:
    
#     print(f"Il Sig. {i}, è invitato a cena!")
#     time.sleep(1)

# print("E' stato trovato un tavolo con altri posti!")
# time.sleep(1)
# dinner.insert(0, "Schubert")
# dinner.insert(2, "Debussy")
# dinner.insert(5, "Lizst")

# for i in dinner:
    
#     print(f"Il Sig. {i}, è invitato a cena!")
#     time.sleep(1)
    
# print(f"La lista degli invitati finali è: {dinner} ")
# time.sleep(1)

# print("Communicazione in arrivo.. ..Tavoli in ritardo..")
# time.sleep(1)

# print("E' necessario disdire gli invitati dalla cena fino ad un massimo di 2 posti!")
# time.sleep(1)

# dinner.pop(5)
# print("Sig. Lizst siamo spiacenti di informarla che la cena è stata annullata.")
# time.sleep(1)

# dinner.pop(4)
# print("Sig. Beethoven siamo spiacenti di informarla che la cena è stata annullata.")
# time.sleep(1)

# dinner.pop(3)
# print("Sig. Mozart siamo spiacenti di informarla che la cena è stata annullata.")
# time.sleep(1)

# dinner.pop(2)
# print("Sig. Debussy siamo spiacenti di informarla che la cena è stata annullata")
# time.sleep(1)

# print(f"La nuova lista degli invitati finali è: {dinner}")
# time.sleep(1)

# for i in dinner:
#     print(f"Il sig. {i} è ancora invitato a cena")
#     time.sleep(1)
    
# del dinner
# dinner = []
# time.sleep(1)
# print(f"{dinner} La lista è vuota")


# # 3-8 Seeing the world:
# import time
# location: list = ["Halstatt", "Wolfgang am see", "Salisburgo", "Innsbruck", "Vienna"]

# # Mostro la lista nel suo ordine originale
# print("Lista originale:")
# print(location)
# time.sleep(2)

# # Ordino la lista in ordine alfabetico crescente con la funzione SORTED
# s = sorted(location)
# print(f"\nLista Ordinata:\n{s}")
# time.sleep(2)

# # Ordino la lista all'incontrario con la funzione SORTED(REVERSE)
# r = sorted(location, reverse = True)
# print(f"\nLista invertita:\n{r}")
# time.sleep(2)

# # Mostro la lista nel suo ordine originale
# print(f"\nLa lista è ancora nel suo ordine originale:\n{location}")
# time.sleep(2)

# # ||Cambio|| l'ordine della lista 
# location.reverse()
# print(f"\nUsato REVERSE per cambiare l'ordine della lista:\n{location}")
# time.sleep(2)

# # ||Ripristino|| l' ordine della lista
# location.reverse()
# print(f"\nL'ordine della lista si è ripristinata:\n{location}")
# time.sleep(2)

# # ||Sistemo|| l' ordine della lista in ordine alfabetico crescente
# location.sort()
# print(f"\nFunzione SORT per sistemare la lista in ordine alfabetico crescente:\n{location}")
# time.sleep(2)

# # ||Sistemo|| l'ordine della lista in ordine alfabetico decrescente
# location.sort(reverse = True)
# print(f"\nFunzione SORT per sistemare la lista in ordine alfabetico decrescente:\n{location}")
# time.sleep(2)


# #3-9: Dinner Guests:
# # names: list = ["a", "b", "c", "d", "e"]
# # print(len(names))
# import time
# dinner: list = ["Chopin", "Mozart", "Bach"]

# for i in dinner:
#     print(f" Sig. {i}, è invitato a cena!")
#     time.sleep(1)

# print(f"{len(dinner)} persone sono state ivitate a cena")

# 3-10: Every Function:
# Creo lista vuota
list = []

# Imposto che il limite massimo di input è 5
for i in range(5):

    # Faccio inserire all'utente 5 preferenze
    user: str = input(f"\nInserire una preferenza {i+1}/5: \n")
    user = list.append(user)

# apro un ciclo di opzioni
while True:

    # Chiedo all'utente cosa vuole fare
    risposta: str = input("\nCosa vuoi fare ora?\n Inserire un opzione tra:\n1Uppercase, Lowercase,")
    

