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

    posizione_tartaruga: int = 1
    posizione_lepre: int = 1
    giocata: int = 1

    print("LET THE GAME BEGIN!!!")
    time.sleep(0.8)
    os.system('clear')
    print("READY!!!")
    print("         _\n     .-./*)\n   _/___\/\n     U U\n")
    time.sleep(0.8)
    os.system('clear')
    print("SET!!!")
    print("""
       _
      (\\\\
       \||
     __(_";
    /    \\
   ()___)\)_
        """)
    time.sleep(0.8)
    os.system('clear')
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    partenza: list[str] = ['_'] * 69
    print('Giocata n', giocata, '|', 'Tarta mossa', pos_t, '|', 'Lepre mossa', pos_l)
    print(f"1°[Tarta pos]= {posizione_tartaruga}\n2°[Lepre pos]= {posizione_lepre}")
    print('TL', *partenza, '\n' * 2)
    print("""
    BBBB  AAAA  N   N  GGGGG   MM MM
    B  B  A  A  NN  N  G       MM MM
    BBB   AAAA  N N N  G  GG   MM MM
    B  B  A  A  N  NN  G   G  
    BBBB  A  A  N   N  GGGGG   MM MM
          """)

    while True:

        time.sleep(1)
        os.system('clear')

        pista: list[str] = ['_'] * 70

        pos_t = tartaruga()
        pos_l = lepre()
        print("!!WHO WILL COME FIRST!!?")
        print('Giocata n', giocata, '|', 'Tarta mossa', pos_t, '|', 'Lepre mossa', pos_l)

        posizione_tartaruga += pos_t
        posizione_lepre += pos_l

        if posizione_tartaruga == posizione_lepre and posizione_tartaruga < 70 and posizione_lepre < 70:

            pista[posizione_lepre - 1] = 'OUCH!!!'

        elif posizione_tartaruga == posizione_lepre and posizione_tartaruga >= 70 and posizione_lepre >= 70:

            os.system('clear')
            print("IT'S A TIE.")
            print('[Tarta pos]=',posizione_tartaruga,'\n', '[Lepre pos]=', posizione_lepre)
            print("""
DDDD   RRRR   AAAAA  W   W
D   D  R   R  A   A  W   W
D   D  RRRR   AAAAA  W W W
D   D  R  R   A   A  WW WW
DDDD   R   R  A   A  W   W
                  """)
            break

        elif posizione_tartaruga >= 70:

            posizione_tartaruga = 70
            os.system('clear')
            print("TORTOISE WINS! || VAY!!!")
            print('1° posizione Tartaruga =',posizione_tartaruga, '\n', '2° posizione Lepre =', posizione_lepre)
            print(
                f"               []# # #  \n"\
                f"         _     || # # # \n"\
                f"     .-./*)    ||# # #  \n"\
                f"   _/___\/     ||       \n"\
                f"     U U       []       \n"\
                )
            break

        elif posizione_lepre >= 70:

            posizione_lepre = 70
            os.system('clear')
            print("HARE WINS || YUCH!!!")
            print('1° posizione: Lepre =',posizione_lepre, '\n', '2° posizione: Tartaruga =', posizione_tartaruga)
            print("""
       _
      (\\\\       []# # #
       \||      || # # #
     __(_";     ||# # #
    /    \\      ||
   ()___)\)_    []
                  """)
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
                print(*pista, '\n')
                print(
f"              \n"
f"              \n"                    
f"              \n"
f"         _    \n"
f"     .-./*)   \n"
f"   _/___\/    \n"
f"     U U      \n"
                )
                continue

            elif posizione_tartaruga < posizione_lepre:
                
                print(f"1°[Lepre pos]= {posizione_lepre}\n2°[Tarta pos]= {posizione_tartaruga}")
                print(*pista, '\n')
                print("""
       _
      (\\\\
       \||
     __(_";
    /    \\
   ()___)\)_
                        """)

            else:

                print(f"1°[Lepre pos]= {posizione_lepre}\n2°[Tarta pos]= {posizione_tartaruga}")
                print(*pista, '\n')
                print("""
     OOO   U   U   CCCC  H   H  [] []
    O   O  U   U  C      H   H  || ||
    O   O  U   U  C      HHHHH  [] []
    O   O  U   U  C      H   H  
     OOO   UUUUU   CCCC  H   H  [] []
                """)

        giocata += 1

gara(tartaruga(), lepre())