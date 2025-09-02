'''
Scrivi un programma in Python che gestisca un magazzino.
Il programma deve permettere di aggiungere prodotti al magazzino,
cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:

    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità.
    Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.

'''

class Prodotto:
    '''
    Definisce una classe Prodotto con i seguenti attributi:
        - nome (stringa)
        - quantità (intero)
    '''

    nome: str
    quantita: int

    def __init__(self, n: str, q: int) -> None:
        self.set_nome(n)
        self.set_quantita(q)

    def set_nome(self, n: str) -> None:
        self.nome = n

    def set_quantita(self, q: int) -> None:
        self.quantita = q

    def get_nome(self) -> str:
        return self.nome

    def get_quantita(self) -> int:
        return self.quantita

    def __str__(self) -> str:
        str_prodotto: str = f"{'Nome: ':<10}{self.get_nome()}\n"\
                            f"{'Quantita ':<10}{self.get_quantita()}"

        return str_prodotto

class Magazzino:
    '''
    Definisce una classe Magazzino con i seguenti metodi:
        - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
        - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
        - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.

    '''

    nome: str
    lista_prodotti: list[Prodotto]

    def __init__(self, n: str) -> None:
        self.set_nome(n)
        self.lista_prodotti = []

    def set_nome(self, n: str) -> None:
        self.nome = n

    def get_nome(self) -> str:
        return self.nome
    
    def aggiungi_prodotto(self, prodotto: Prodotto) -> None:
        '''
        - aggiunge un prodotto al magazzino
        '''

        if prodotto not in self.lista_prodotti:
            self.lista_prodotti.append(prodotto)

        else:
            for p in self.lista_prodotti:

                if p.get_nome() == prodotto.get_nome():
                    p.set_quantita(prodotto.get_quantita() + p.get_quantita())
                    break

    def cerca_prodotto(self, nome: str) -> Prodotto:
        '''
        - cerca un prodotto per nome e lo ritorna se esiste.
        '''

        for p in self.lista_prodotti:

            if p.get_nome() == nome:
                return p
        
        return None

    def verifica_disponibilita(self, nome: str) -> str:
        '''
        - verifica se un prodotto è disponibile in magazzino.
        '''

        for p in self.lista_prodotti:

            if nome == p.get_nome():
                prodotto_str: str = f"{p.get_quantita()} {'rimanenti' if p.quantita > 1 else 'rimanente'} in magazzino"

                return prodotto_str
        
        return f"Nessun prodotto {nome} nell'inventario"

if __name__ == "__main__":

    prodotto1: Prodotto = Prodotto("Astuccio", 10)
    prodotto2: Prodotto = Prodotto("Astuccio", 20)
    prodotto3: Prodotto = Prodotto("Quaderno", 1)

    print(prodotto1.get_quantita())
    prodotto1.set_quantita(15)
    print(prodotto1.get_quantita())

    magazzino1: Magazzino = Magazzino("Mgz1")
    magazzino1.aggiungi_prodotto(prodotto1)
    magazzino1.aggiungi_prodotto(prodotto1)

    magazzino1.aggiungi_prodotto(prodotto2)
    print(prodotto1.get_quantita())

    print(magazzino1.verifica_disponibilita("Astuccio"))
    magazzino1.aggiungi_prodotto(prodotto3)
    print(magazzino1.verifica_disponibilita("Quaderno"))
    print(magazzino1.verifica_disponibilita("Diario"))


    print(magazzino1.cerca_prodotto("Quaderno"))