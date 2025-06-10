'''
Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.
'''

def check(x: bool, y: bool, z: bool) -> str:
    # if y == True or z == True and x == True: <- mio
    #     return "Azione Permessa"
    if x and(y or z):                         #<- prof
        return "Azione Permessa"

    else:
        return "Azione negata"