'''
Every Function:
'''

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