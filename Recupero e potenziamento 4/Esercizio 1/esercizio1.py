'''
Esercizio 1.
 
Nota.
Questo esercizio è da svolgere prima tramite diagramma a blocchi,
effettuando un check numerico per verificare che i risultati prodotti dal vostro algoritmo
siano uguali a quelli dell'expected output proposto nella traccia.
Quando il docente darà il permesso, ogni studente provvederà a tradurre l'algoritmo elaborato in codice Python.
Durante lo svolgimento dell'esercizio non è possibile confrontarsi con gli altri compagni di corso.
Qualora sia necessario, chiedere eventuali chiarimenti al docente.
 
Un garage fa pagare una tariffa minima di 2.00 $ per parcheggiare fino a tre ore,
più 0.50 $ all'ora per ogni ora o parte di essa oltre le tre ore.
Il costo per un periodo di 24 ore di parcheggio ammonta a 10.00 $. Supponete che nessuna macchina resti parcheggiata per più di 24 ore.
Elaborare un algoritmo che calcoli e stampi i costi del parcheggio per una dato periodo di tempo.
 
Una volta elaborato l'algoritmo, scrivere in Python, una funzione calculateCharges()
che consenta di determinare il costo del parcheggio per un dato cliente.
 
Scrivere un codice Python che consenta di calcolare i costi del parcheggio per ciascuno dei quattro clienti
che ieri hanno parcheggiato le loro auto in questo garage. Mostra, poi, i risultati in forma tabellare.
Il vostro output deve avere il seguente formato:

Car        Hours           Charge
 1           1.5            2.00 $
 2           4.0            2.50 $
 3          5.50            3.50 $
 4          24.0           10.00 $        
 TOTAL      35.0           17.50 $ 
'''
import math
def calculateCharges(insertH: int | float) -> float:

    tariffa_minima: float = 2.00 # fino a 3 ore
    tariffa_aggiuntiva: float = 0.50 # all'ora dopo le prime 3 (3.1 in poi)
    tariffa_giornaliera: float = 10.00

    if insertH <= 3:
        return tariffa_minima

    elif insertH > 3 and insertH < 24:

        if isinstance(insertH, float):
            insertH = math.ceil(insertH - 3)   

        return tariffa_minima + tariffa_aggiuntiva * insertH # if insertH%1 != 0 else tariffa_minima + (insertH - 3)*0.5

    else:
        return tariffa_giornaliera if insertH == 24 else "Fuori range!"
if __name__ == "__main__":

    car1: float = calculateCharges(1.5)
    car2: float = calculateCharges(4.0)
    car3: float = calculateCharges(5.50)
    car4: float = calculateCharges(24)

    total: float = car1 + car2 + car3 + car4
    hours: float = 1.5 + 4.0 + 5.50 + 24

    # TABELLA PROF    

    cars: list[float] = [1.5 , 4.0, 5.50, 24]

    print(f"{'car':<10} {'hour':<10} {'charges':<10}")
    for i in range(len(cars)):

        t = calculateCharges(cars[i])
        print(f"{i + 1:<10} {cars[i]:<10} {t:<.2f}")

    print(f"{'TOTAL':<10} {sum(cars):<10} {total:<10}")






    



    # print(
    #     f'''
    # Car         Hours           Charge
    # 1                  1.5             {p1} $
    # 2                 4.0             {p2} $
    # 3               5.50             {p3} $
    # 4               24.0           {p4} $
    # TOTAL      35.0           {total} $
    #     '''
    # )