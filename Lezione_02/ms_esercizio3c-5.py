user_nome: str = (input("Digitare nome dell'utente: "))
user_ruolo: str = (input("Digitare ruolo dell'utente: "))
user_eta: str = (input("Digitare l'età dell'utente: "))

dizionario: dict[str:str and int] = {"nome": user_nome,"ruolo": user_ruolo, "età": user_eta}

match dizionario:

    case {"nome": user_nome,"ruolo": "admin", "età": user_eta}:

        print("Accesso completo a tuttle le funzionalità.")