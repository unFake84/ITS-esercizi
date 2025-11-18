'''
Esercizi su url_for()

    Generazione link interni

        Usare url_for() per creare automaticamente i link
        alle route definite,
        ed esporli in una pagina principale
        (homepage con link a /about, /users/..., ecc.).

    Navigazione dinamica

        Creare una pagina con elenco utenti fittizi e
        i relativi link ai loro profili generati con url_for().

    Mini blog

        Definire route /posts/<int:id> che restituisca
        un articolo fittizio.

        Creare una pagina /posts con un elenco di post e
        i relativi link agli articoli generati tramite url_for().

'''

from flask import Flask, url_for

app: Flask = Flask(__name__)

@app.route('/posts/<int:id>')
def articolo_fittizio(id: int) -> str:

    return f"Pagina {id}"

@app.route('/posts')
def articoli() -> str:

    urlPosts: list[int] = []
    for id_s in range(1, 11):

        urlPosts.append(url_for('articolo_fittizio', id=id_s))

    return urlPosts

if __name__ == "__main__":

    app.run(debug=True)