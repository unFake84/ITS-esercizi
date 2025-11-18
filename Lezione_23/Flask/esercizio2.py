'''
Esercizi su routing statico e dinamico

    Route dinamica per profilo utente

        Creare un percorso /users/<nome> che restituisca “Benvenuto, <nome>!”.

        Testare con nomi diversi nell’URL.

    Route con parametri numerici

        Definire /square/<int:n> che ritorni una stringa contenente n e il suo quadrato.

    Parametri multipli

        Creare /sum/<int:a>/<int:b> che restituisca una stringa contenente a, b, e la somma dei due numeri.

'''

from flask import Flask

app: Flask = Flask(__name__)

@app.route("/users/<string:nome>")
def bienvenue(nome: str) -> str:

    return f"""   
<div style="margin: 300px auto;
            width: 50%;
            text-align: center;">           
    <p style="color: orange;">
        Benvenuto<br/>
        {nome}
    </p>
</div>
"""

if __name__ == "__main__":

    app.run(debug=True)