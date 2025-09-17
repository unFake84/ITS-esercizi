'''
### CLASSE: Fattura
Creare un file chiamato "fatture.py".
In tale file, creare una classe chiamata Fattura.

- Definire i seguenti metodi:

    init(patient,doctor):
    Deve avere come input una lista di pazienti ed un dottore.
    Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor().
    In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore,
    mentre assegnare 0 all'attributo salary (di tipo int).
    In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore,
    come, ad esempio:
    "Non è possibile creare la classe fattura poichè il dottore non è valido!".

    getSalary():
    Deve ritornare il salario guadagnato dal dottore.
    Il salario guadagnato viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.

    getFatture():
    Deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e
    ritornare il suo valore.

    addPatient(newPatient)
    Consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario,
    richiamando il metodo getFatture() e getSalary().
    Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"

    removePatient(idCode):
    Consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo
    del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary().
    Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
'''

####### __salary è int ma in realtà è un float
####### controllare i metodi che utilizzano gli attributi che possono diventare None (prevenire)
####### completare __str__ (facoltativo)

from dottore import Doctor
from paziente import Patient

class Bill:

    __patient: list[Patient]
    __doctor: Doctor
    __invoice: int
    __salary: int

    def __init__(self, patient: list[Patient], doctor: Doctor) -> None:
        if doctor.getAge() > 30:
            doctor.isAValidDoctor()
            self.__invoice = len(patient)
            self.__salary = 0
            self.__patient = patient
            self.__doctor = doctor

        else:
            self.__patient = None
            self.__doctor = None
            self.__invoice = None
            self.__salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
    
    def getSalary(self) -> int:
        return self.__doctor.getParcel() * self.__invoice
    
    def getDoctor(self) -> Doctor:
        return self.__doctor

    def addPatient(self, newPatient: Patient) -> None:
        id_list: list[str] = [id_p.getIdCode() for id_p in self.__patient]

        if newPatient.getIdCode() not in id_list:
            self.__patient.append(newPatient)
            self.__invoice += 1
            self.getSalary()
            doctor: Doctor = self.getDoctor()
            print(f"Alla lista del Dottor {doctor.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}")
    
    def removePatient(self, idCode: str) -> None:
        for patient in self.__patient:
            
            if patient.getIdCode() == idCode:
                self.__patient.remove(patient)
                self.__invoice -= 1
                self.getSalary()
                doctor: Doctor = self.getDoctor()
                print(f"Alla lista del Dottor {doctor.getLastName()} è stato rimosso il paziente {idCode}")

    # def __str__(self) -> str:
    #     patient_list: list[str] = '\n'.join([p.getName() for p in self.__patient])
    #     return patient_list

if __name__ == "__main__":

    p1: Patient = Patient("Mario", "Merio", "001")
    p2: Patient = Patient("Bibo", "Bobi", "002")
    p3: Patient = Patient("Geronio", "Lo Becio", "003")

    l_p: list[Patient] = [p1, p2, p3]

    d1: Doctor = Doctor("Pino", "Micio", "Piediatra", 97.5)
    d1.setAge(31)

    fattura1: Bill = Bill(l_p, d1)

    print(fattura1.getSalary())         # 292.50

    p4: Patient = Patient("Gesualdo", "Rotocalchini", "004")
    fattura1.addPatient(p4)

    print(fattura1.getSalary())         # 390.00

    fattura1.removePatient("002")

    print(fattura1.getSalary())         # 292.50

    #print(fattura1)