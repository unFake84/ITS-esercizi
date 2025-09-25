'''
Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo.
Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e
il numero della carta di credito.
Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito
oltre all'importo del pagamento.
'''

from pagamento import Pagamento

class PagamentoCartaDiCredito(Pagamento):

    __titolare_carta: str
    __data_di_scadenza: str
    __numero_carta: str

    def __init__(
            self,
            importo: int|float,
            titolare_carta: str,
            data_scadenza: str,
            numero_carta: str
                 ) -> None:
        super().__init__()

        self.setImporto(importo)
        self.__titolare_carta = titolare_carta
        self.__data_di_scadenza = data_scadenza
        self.__numero_carta = numero_carta

    def dettagliPagamento(self) -> str:
        return f"Pagamento di: €{self.getImporto():.2f} effettuato con la carta di credito\nNome sulla carta: {self.__titolare_carta}\nData di scadenza: {self.__data_di_scadenza}\nNumero della carta: {self.__numero_carta}"