user_eta: int = (int(input("Inserire età: ")))

if user_eta < 18 or user_eta > 65:

    if user_eta < 18:

        print("Non puoi partecipare all'attività "
        "perchè non hai raggiunto l'età minima richiesta.")

    else:

        print("Non puoi partecipare all'attività "
        "perchè hai superato l'età massima consentita")

else:

    print("Puoi partecipare all'attività.")