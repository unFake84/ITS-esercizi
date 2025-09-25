'''
Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con
valori differenti e si invochi dettagliPagamento() per ognuno di essi.

Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321
'''

from pagamentocontanti import PagamentoContanti
from pagamentocartadicredito import PagamentoCartaDiCredito

pc1: PagamentoContanti = PagamentoContanti(150.00)
pc2: PagamentoContanti = PagamentoContanti(95.25)

pcdc1: PagamentoCartaDiCredito = PagamentoCartaDiCredito(200, "Mario Rossi", "12/24", "1234567890123456")
pcdc2: PagamentoCartaDiCredito = PagamentoCartaDiCredito(500, "Luigi Bianchi", "01/25", "6543210987654321")

print(pc1.dettagliPagamento())
pc1.inPezziDa()
print("")
print(pc2.dettagliPagamento())
pc2.inPezziDa()
print("")
print(pcdc1.dettagliPagamento())
print("")
print(pcdc2.dettagliPagamento())