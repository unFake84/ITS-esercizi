import time
import random
import os

def tartaruga(pos: int = 1):

    mossa: int = random.randint(1, 10)

    if mossa <= 5:

        # aumenta 3 quadrati, passo veloce
        pos += 3

    elif mossa >= 6 and mossa <= 7:

        # scivolata, arretra 6 quadrati (no sotto l'1)
        pos -= 6

    elif mossa >= 8:

        # aumenta 1 quadrato, passo lento
        pos += 1

    return pos

def lepre(pos: int = 1):

    mossa: int = random.randint(1,10)

    if mossa >= 3 and mossa <= 4:

        # avanza di 9 quadrati, grande balzo
        pos += 9 

    elif mossa == 5:

        # arretra di 12 posizioni, grande scivolata
        pos -= 12

    elif mossa >= 6 and mossa <=8:

        # avanza di un quadrato, piccolo balzo
        pos += 1

    elif mossa >= 8 and mossa <= 10:

        # arretra di 2 quadrati (no sotto l'1), piccola scivolata
        pos -= 2

    return pos

def gara(pos_t: int, pos_l: int):

    posizione_tartaruga: int = 0
    posizione_lepre: int = 0
    giocata: int = 1

    print("LET THE GAME BEGIN!!!")
    time.sleep(0.8)
    os.system('clear')
    print("READY!!!")
    time.sleep(0.8)
    os.system('clear')
    print("SET!!!")
    time.sleep(0.8)
    os.system('clear')
    print("BANG !!!!! AND THEY'RE OFF !!!!!")

    while True:

        time.sleep(1)
        os.system('clear')

        pista: list[str] = ['_'] * 70

        pos_t = tartaruga()
        pos_l = lepre()
        print('Giocata n', giocata, '|', 'Tarta mossa', pos_t, '|', 'Lepre mossa', pos_l)

        posizione_tartaruga += pos_t
        posizione_lepre += pos_l

        if posizione_tartaruga == posizione_lepre and posizione_tartaruga < 70 and posizione_lepre < 70:

            pista[posizione_lepre - 1] = 'OUCH!!!'

        elif posizione_tartaruga == posizione_lepre and posizione_tartaruga >= 70 and posizione_lepre >= 70:

            print("IT'S A TIE.")
            print('[Tarta pos]=',posizione_tartaruga,'\n', '[Lepre pos]=', posizione_lepre)
            break

        elif posizione_tartaruga >= 70:

            posizione_tartaruga = 70
            print("TORTOISE WINS! || VAY!!!")
            print('[Tarta pos]=',posizione_tartaruga,'\n', '[Lepre pos]=', posizione_lepre)
            break

        elif posizione_lepre >= 70:

            posizione_lepre = 70
            print("HARE WINS || YUCH!!!")
            print('[Tarta pos]=',posizione_tartaruga,'\n', '[Lepre pos]=', posizione_lepre)
            break
        
        elif posizione_tartaruga < 1:

            posizione_tartaruga = 1
            pista[posizione_tartaruga - 1] = 'T'
            pista[posizione_lepre - 1] = 'L'

        elif posizione_lepre < 1:

            posizione_lepre = 1
            pista[posizione_lepre - 1] = 'L'
            pista[posizione_tartaruga - 1] = 'T'

        elif posizione_tartaruga != posizione_lepre:

            pista[posizione_tartaruga - 1] = 'T'
            pista[posizione_lepre - 1] = 'L'

        #print('Tarta',pos_t,'\n', 'Lepre', pos_l)
        if giocata:
            
            if posizione_tartaruga > posizione_lepre:

                print(f"1°[Tarta pos]= {posizione_tartaruga}\n2°[Lepre pos]= {posizione_lepre}")

            else:

                print(f"1°[Lepre pos]= {posizione_lepre}\n2°[Tarta pos]= {posizione_tartaruga}")

        print(*pista)
        giocata += 1

gara(tartaruga(), lepre())