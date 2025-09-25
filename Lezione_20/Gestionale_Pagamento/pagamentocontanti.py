'''
Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo.
Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti.
Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da
500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o
in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono
necessarie per pagare l'importo in contanti.
'''

from pagamento import Pagamento

class PagamentoContanti(Pagamento):

    def __init__(self, importo: int|float) -> None:
        super().__init__()

        self.setImporto(importo)

    def dettagliPagamento(self) -> str:
        return f"Pagamento in contanti di: €{self.getImporto():.2f}"

    def inPezziDa(self) -> None:
        importo: float = self.getImporto()
        banconoteEmonete: list[int] = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.20, 0.10, 0.05, 0.01]

        print(f"{importo:.2f} euro da pagare in contanti con:")
        for taglio in banconoteEmonete:

            n: int = int(importo // taglio)

            if n > 0:

                print(f"{n} {'banconota' if n == 1 else 'banconote'} da {taglio}")\
                    if taglio >= 5 else\
                        print(f"{n} {'moneta' if n == 1 else 'monete'} da {taglio}")

            importo = round(importo - n * taglio, 2)

if __name__ == "__main__":

    pc1: PagamentoContanti = PagamentoContanti(425.10)
    # pc1.setImporto(80.0)
    pc1.inPezziDa()