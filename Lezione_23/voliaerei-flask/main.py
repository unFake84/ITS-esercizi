from flask import Flask, jsonify
from db.utils import load_data_from_db
from flask.typing import ResponseReturnValue

app = Flask(__name__)

@app.route('/')
def initial_message():

    return jsonify({"response":'Questo è il messaggio di benvenuto'})

@app.route('/nazioni', methods=['GET'])
def get_nazioni() -> ResponseReturnValue|None:

    dati = load_data_from_db() # carica TUTTI i dati dal finto database nel file json
    nazioni: dict[str, dict[str, str]] = dati['Nazione']
    return jsonify(nazioni), 200

@app.route('/db', methods=['GET'])
def getAllDb() -> ResponseReturnValue|None:

    dati = load_data_from_db() # carica TUTTI i dati dal finto database nel file json
    return jsonify(dati), 200

@app.route('/citta', methods=['GET'])
def getCities() -> ResponseReturnValue|None:

    dati = load_data_from_db()
    citta: dict[str, dict[str, str|int]] = dati['Citta']
    return jsonify(citta), 200

@app.route('/compagnie', methods=['GET'])
def getCompanies() -> ResponseReturnValue|None:

    dati = load_data_from_db()
    companies: dict[str, dict[str, str|int]] = dati['Compagnia']
    return jsonify(companies), 200

@app.route('/voli', methods=['GET'])
def getFlights() -> ResponseReturnValue|None:

    dati = load_data_from_db()
    flights: dict[str, dict[str, str|int]] = dati['Volo']
    return jsonify(flights), 200

@app.route('/aeroporti', methods=['GET'])
def getAirport() -> ResponseReturnValue|None:

    dati = load_data_from_db()
    airports: dict[str, dict[str, str|int]] = dati['Aeroporto']
    return jsonify(airports), 200

if __name__ == "__main__":
    app.run(debug=True)