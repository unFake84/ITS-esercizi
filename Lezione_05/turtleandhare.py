import time
import random
import os

def tartaruga(pos: int = 1):

    mossa: int = random.randint(1, 10)

    if mossa <= 5:

        # aumenta 3 quadrati, passo veloce
        pos += 3

    elif mossa >= 6 and mossa <= 7:

        # scivolata, arretra 6 quadrati
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

        # arretra di 2 quadrati, piccola scivolata
        pos -= 2

    return pos

def gara(pos_t: int, pos_l: int):

    posizione_tartaruga: int = 1
    posizione_lepre: int = 1
    giocata: int = 1
    controllo: bool = False
    minuti: int = 0
    secondi: int = 0

    while True:

        secondi += 1

        if secondi == 60:

            minuti += 1
            secondi = 0

        if giocata == 1:

            print("LET THE GAME BEGIN!!!")
            time.sleep(1.2)
            os.system('clear')

            print("READY!!!")
            print("         _\n     .-./*)\n   _/___\/\n     U U\n")
            time.sleep(0.7)
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
            time.sleep(0.7)
            os.system('clear')

            print("BANG !!!!! AND THEY'RE OFF !!!!!")

            partenza: list[str] = ['_'] * 69

            print('Giocata n', giocata, '|', 'Tarta mossa', pos_t, '|', 'Lepre mossa', pos_l)
            print(f"1° pos[Tarta]= {posizione_tartaruga}\n2° pos [Lepre]= {posizione_lepre}")
            print(f"Tempo di gara: min {minuti}:{secondi} sec\n")
            print('TH', *partenza, '\n' * 2)
            print("""
            BBBB  AAAA  N   N  GGGGG   MM MM
            B  B  A  A  NN  N  G       MM MM
            BBB   AAAA  N N N  G  GG   MM MM
            B  B  A  A  N  NN  G   G  
            BBBB  A  A  N   N  GGGGG   MM MM
            """)

            giocata += 1
            secondi += 1

        time.sleep(1)
        os.system('clear')

        pista: list[str] = ['_'] * 70

        pos_t = tartaruga() -1
        pos_l = lepre() -1

        print("!!WHO WILL COME FIRST!!?")
        print('Giocata n', giocata, '|', 'Tarta mossa', pos_t, '|', 'Lepre mossa', pos_l)

        posizione_tartaruga += pos_t
        posizione_lepre += pos_l
        max_tarta: int = posizione_tartaruga
        max_lepre: int = posizione_lepre

        if posizione_tartaruga == posizione_lepre and posizione_tartaruga < 70 and posizione_lepre < 70:

            pista[posizione_lepre - 1] = 'OUCH!!!'

        elif posizione_tartaruga >= 70 and posizione_lepre >= 70:

            controllo = True

            time.sleep(1)
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

            if minuti == 0:

                print(f"Durata gara: {secondi} secondi.")

            elif minuti > 1:

                if secondi == 1:

                    print(f"Durata gara: {minuti} minuti e {secondi} secondo.")

                print(f"Durata gara: {minuti} minuti e {secondi} secondi.")

            elif minuti > 0:

                if secondi == 0:

                    print(f"Durata gara: {minuti} minuto.")

                else:

                    print(f"Durata gara: {minuti} minuto e {secondi} secondi.")
            
            interruttore: int = 1

            while interruttore == 1:
                
                    user: str = (input("Ricominciare?: "))

                    if user == 'no':
                    
                        interruttore = 0                    

                    elif user != 'si':

                        print("""
      Risposta non valida
    Per chiudere digitare 'no'.
    Per riavviare digitare 'si'.
                        """)

                    elif user == 'si':

                        interruttore = 0
                    
            if interruttore == 0 and user == 'no':

                break

            elif interruttore == 0 and user == 'si':

                posizione_tartaruga = 1
                posizione_lepre = 1
                giocata = 1
                secondi = 0
                minuti = 0
                time.sleep(2)
                os.system('clear')

        elif posizione_tartaruga >= 70:

            controllo = True
            posizione_tartaruga = 70

            time.sleep(1)
            os.system('clear')

            print("TORTOISE WINS! || VAY!!!")
            print('1° posizione Tartaruga =',posizione_tartaruga, '\n', '2° posizione Lepre =', posizione_lepre)
            print("""

     _..---.--.
   .'\ __|/O.__)       []# # #
  /__.' _/ .-'_\\       || # # # 
 (____.'.-_\____)      ||# # # 
  (_/ _)__(_ \_)\_     || 
   (_..)--(.._)'--'    []

""")
            print(f"Risultato finale: {max_tarta} vs {max_lepre}")

            if minuti == 0:

                print(f"Durata gara: {secondi} secondi.")

            elif minuti > 1:

                if secondi == 1:

                    print(f"Durata gara: {minuti} minuti e {secondi} secondo.")

                print(f"Durata gara: {minuti} minuti e {secondi} secondi.")

            elif minuti > 0:

                if secondi == 0:

                    print(f"Durata gara: {minuti} minuto.")

                else:

                    print(f"Durata gara: {minuti} minuto e {secondi} secondi.")
            
            interruttore: int = 1

            while interruttore == 1:
                
                    user: str = (input("Ricominciare?: "))

                    if user == 'no':
                    
                        interruttore = 0                    

                    elif user != 'si':

                        print("""
      Risposta non valida
    Per chiudere digitare 'no'.
    Per riavviare digitare 'si'.
                        """)

                    elif user == 'si':

                        interruttore = 0
                    
            if interruttore == 0 and user == 'no':

                break

            elif interruttore == 0 and user == 'si':

                posizione_tartaruga = 1
                posizione_lepre = 1
                giocata = 1
                secondi = 0
                minuti = 0
                time.sleep(2)
                os.system('clear')

        elif posizione_lepre >= 70:

            controllo = True
            posizione_lepre = 70

            time.sleep(1)
            os.system('clear')

            print("HARE WINS || YUCH!!!")
            print('1° posizione: Lepre =',posizione_lepre, '\n', '2° posizione: Tartaruga =', posizione_tartaruga)
            print("""

      _     _
     ( |\  //|     []# # #
      \|\\\\//\|     || # # #
        /66\\       ||# # #
       ((_v.)      ||
        > "<       []
""")
            print(f"Risultato finale: {max_lepre} vs {max_tarta}")

            if minuti == 0:

                print(f"Durata gara: {secondi} secondi.")

            elif minuti > 1:

                if secondi == 1:

                    print(f"Durata gara: {minuti} minuti e {secondi} secondo.")

                print(f"Durata gara: {minuti} minuti e {secondi} secondi.")

            elif minuti > 0:

                if secondi == 0:

                    print(f"Durata gara: {minuti} minuto.")

                else:

                    print(f"Durata gara: {minuti} minuto e {secondi} secondi.")
            
            interruttore: int = 1

            while interruttore == 1:
                
                    user: str = (input("Ricominciare?: "))

                    if user == 'no':
                    
                        interruttore = 0                    

                    elif user != 'si':

                        print("""
      Risposta non valida
    Per chiudere digitare 'no'.
    Per riavviare digitare 'si'.
                        """)

                    elif user == 'si':

                        interruttore = 0
                    
            if interruttore == 0 and user == 'no':

                break

            elif interruttore == 0 and user == 'si':

                posizione_tartaruga = 1
                posizione_lepre = 1
                giocata = 1
                secondi = 0
                minuti = 0
                time.sleep(2)
                os.system('clear')
        
        elif posizione_tartaruga < 1:

            posizione_tartaruga = 1
            pista[posizione_tartaruga - 1] = 'T'
            pista[posizione_lepre - 1] = 'H'

        elif posizione_lepre < 1:

            posizione_lepre = 1
            pista[posizione_lepre - 1] = 'H'
            pista[posizione_tartaruga - 1] = 'T'

        elif posizione_tartaruga != posizione_lepre:

            pista[posizione_tartaruga - 1] = 'T'
            pista[posizione_lepre - 1] = 'H'

        #print('Tarta',pos_t,'\n', 'Lepre', pos_l)
        if controllo == False:
            
            if posizione_tartaruga > posizione_lepre:
                
                print(f"1° pos [Tarta]= {posizione_tartaruga}\n2° pos [Lepre]= {posizione_lepre}")
                print(f"Tempo di gara: min {minuti}:{secondi} sec \n")
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

            elif posizione_tartaruga < posizione_lepre:
                
                print(f"1° pos [Lepre]= {posizione_lepre}\n2° pos [Tarta]= {posizione_tartaruga}")
                print(f"Tempo di gara: min {minuti}:{secondi} sec \n")
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

                print(f"1° pos [Lepre]= {posizione_lepre}\n2° pos [Tarta]= {posizione_tartaruga}")
                print(f"Tempo di gara: min {minuti}:{secondi} sec \n")
                print(*pista, '\n')
                print("""
     OOO   U   U   CCCC  H   H  [] []
    O   O  U   U  C      H   H  || ||
    O   O  U   U  C      HHHHH  [] []
    O   O  U   U  C      H   H  
     OOO   UUUUU   CCCC  H   H  [] []
                """)

        elif controllo == True:

            controllo = False
            giocata = 0

        giocata += 1

gara(tartaruga(), lepre())