'''
Esercizio di base

    Definire un route /about

        Definire una route /about che ritorni un breve testo HTML con descrizione dell’app o dell’autore.

'''

from flask import Flask

app = Flask(__name__)       #<- Crea il server Flask e lo collega al file in cui mi trovo.

@app.route("/about")        #<- Se qualcuno visita /about, esegue questa funzione e mostra il suo risultato nel browser.
def testo() -> str:         #<- È la funzione che gestisce la richiesta.
    
    return """   
<div style="margin: 300px auto;
            width: 50%;
            text-align: center;">           
    <p style="color: orange;">
        Funziona così?<br/>
        A quanto pare si!
    </p>
</div>
"""                         #<- Flask accetta come risposta una semplice stringa contenente HTML — e la mostra nel browser.

if __name__ == "__main__":                            
    app.run(debug=True)     #< -Serve per avviare il server di sviluppo di Flask:
                            #       debug=True consente di vedere errori dettagliati
                            #       Riavvia automaticamente l’app se si cambia il codice.