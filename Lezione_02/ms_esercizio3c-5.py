user_nome: str = (input("Digitare nome dell'utente: "))
user_ruolo: str = (input("Digitare ruolo dell'utente: "))
user_eta: str = (input("Digitare l'età dell'utente: "))

dizionario: dict[str:str and int] = {"nome": user_nome,"ruolo": user_ruolo, "età": user_eta}

match dizionario:

    case {"ruolo": "admin"}:

        print("Accesso completo a tuttle le funzionalità.")

    case {"ruolo": "moderatore"}:

        print("Accesso standard a tutti i servizi.")

    case {"ruolo": user_ruolo, "eta": user_eta} if user_eta >= 18:

        print("Accesso standard a tutti i servizi.")

    case {"ruolo": user_ruolo, "eta": user_eta} if user_eta < 18:

        print("Accesso limitato! Alcune funzionalità sono bloccate.")

    case {"ruolo": user_ruolo}:

        print("Accesso ristretto! Solo visualizzazione dei contenuti.")

    case _:

        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")