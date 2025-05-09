import json

PATH: str = "Lezione_15/Jsons/config.json" # SELEZIONARE NOME DA MODIFICARE/CREARE
mode: str = "r"
encoding: str = "utf-8"



# MODIFICARE UN FILE -INIZIO-----------------------
# config = None

# def connect(host, port):

#     #
#     print(f"Connected to {host}:{port}")

# with open(PATH, mode=mode, encoding=encoding) as file:

#     config: dict = json.load(file)

# config["AGGIUNTA"] = "NUOVO"
# config["server"]["host"] = "google.it"
# MODIFICARE UN FILE -FINE-----------------------



# CREARE UN FILE -INIZIO-----------------------
config: dict = {"GRGFLV...": {"name": "Dioni", "last_name": "Manon", "age": 40}}
# CREARE UN FILE -FINE-----------------------



with open(PATH, mode="w") as file:

    json.dump(config, file, indent=4) # =buttalo



# #
# print(f'Host: {config["server"]["host"]} Port: {config["server"]["port"]}')

# #
# connect(host=config["server"]["host"], port=config["server"]["port"])