from typing import Any

user_nome: str = (input("Digitare nome dell'utente: "))
user_ruolo: str = (input("Digitare ruolo dell'utente: "))
user_eta: int = (int(input("Digitare l'età dell'utente: ")))

dizionario: dict[str, Any] = {"nome": user_nome,"ruolo": user_ruolo, "età": user_eta}

match dizionario:

    case {"ruolo": "admin"}:

        print("Accesso completo a tuttle le funzionalità.")

    case {"ruolo": "moderatore"}:

        print(f"Salve {user_nome}! Può gestire i contenuti ma non modificare le impostazioni.")

    case {"ruolo": "utente"} if user_eta >= 18:

        print("Accesso standard a tutti i servizi.")

    case {"ruolo": "utente"} if user_eta >= 1 and user_eta < 18:

        print("Accesso limitato! Alcune funzionalità sono limitate!")

    case {"ruolo": "ospite"}:

        print("Accesso ristretto! Solo visualizzazione dei contenuti.")

    case _:

        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")