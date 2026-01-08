from flask import Flask, jsonify, url_for

from main import Ride
from main import parco1

app = Flask(__name__)

@app.route("/")
def index():
    '''
    GET /

    Restituisce un json con:

        una breve descrizione del servizio (es. "Welcome to Park API"),
        alcuni link testuali che indicano le altre route disponibili (es. "/rides", "/rides/rc1", "/rides/rc1/wait/4.0").
        Devi generare i link dinamicamente con url_for() e poi inserirli nel json.
    '''
    return jsonify({
        "descrizione": "Welcome_to_Park_API",
        "altri_link": {
            "tutte_le_giostre": url_for("lista_giostre"),
            "giostra_1": url_for('prendi', id = "1"),
            "giostra_2": url_for('prendi', id = "2"),
            "tempo_attesa_giostra_1": url_for("tempo_attesa", id = 1),
            "tempo_attesa_giostra_2": url_for("tempo_attesa", id = 2)
        }
    })

@app.route("/rides")
def lista_giostre():
    '''
    GET /rides

    Restituisce un json di attrazioni presenti nel parco.
    Ogni elemento del json può essere:

        una stringa descrittiva (es. "rc1 - Vortex (roller_coaster) - min 140cm"), oppure
        un dizionario con i campi principali dell’attrazione.
    '''
    info_giostre: list[dict[str, str|int]] = parco1.list_all()
    return jsonify(info_giostre)

@app.route("/rides/<string:id>")
def prendi(id: str):
    '''
    GET /rides/<ride_id>

    Restituisce un json con un solo elemento che rappresenta i dettagli dell’attrazione con l’ID specificato.
    '''
    ride: Ride = parco1.get(id)
    
    if ride is None:
        return jsonify({"errore": "giostra non trovata"})
    
    return jsonify(ride.info())

@app.route("/rides/<string:id>/wait", defaults = {"crowd": 1.0})
@app.route("/rides/<string:id>/wait/<float:crowd>")
def tempo_attesa(id: str, crowd: float):
    '''
    GET /rides/<ride_id>/wait/crowd

    Restituisce un json con le informazioni sull’attesa stimata per l’attrazione specificata.

        Il parametro crowd è facoltativo e indica un fattore di affollamento (di default 1.0).
        L’output può essere, ad esempio, una json contenente una stringa "Attesa: 60 minuti" oppure un dizionario {"wait_min": 60}.
    '''
    ride: Ride = parco1.get(id)

    if ride is not None:
        wait: int = ride.wait_time(crowd)
        return jsonify({"tempo_attesa": wait})
    
    return jsonify({"errore": "giostra non trovata"})

if __name__ == "__main__":
    app.run(debug=True)