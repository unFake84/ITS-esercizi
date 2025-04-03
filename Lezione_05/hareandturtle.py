import time
import random
import os

def tartaruga(pos: int = 0):

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

def lepre(pos: int = 0):

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
    iterazionitot: int = 0
    secondi: int = 1
    meteo: bool = False
    terreno: list[str] = [".",".",",",",",".","Y",".",".",","]
    decimosecondo: int = 1
    interruttore: int = 1
    gestionemeteo = 0
    t: str = "Tarta🐢"
    l: str = "Lepre🐇"

    while True:

        iterazionitot += 1

        if iterazionitot%10 == 0:
            
            secondi += 1
            giocata += 1

        if giocata == 1:

            os.system('clear')

            #print(f"gestionemeteo [{gestionemeteo}]----pos_t [{pos_t}]----pos_l [{pos_l}]----dieciminuti {iterazionitot}")

            print("")
            print("LET THE GAME BEGIN!!!", "\n" * 30)
            time.sleep(1.5)
            os.system('clear')

            print("")
            print("READY!!!")
            print("         _\n     .-./*)\n   _/___\/\n     U U\n", "\n" * 25)
            time.sleep(1)
            os.system('clear')

            print("")
            print("SET!!!")
            print("""
        _
       (\\\\
        \||
      __(_";
     /    \\
    ()___)\)_
                """, "\n" * 22)
            time.sleep(1)
            os.system('clear')

            print("BANG !!!!! AND THEY'RE OFF !!!!!")
            
            partenza: list[str] = ['_'] * 72 

            print('Giocata n', giocata, '|', 'Tarta mossa', pos_t, '|', 'Lepre mossa', pos_l)
            print(f"1° pos[Tarta]= {posizione_tartaruga}\n2° pos [Lepre]= {posizione_lepre}")
            print(f"Tempo di gara: min 0{minuti}:0{secondi} sec\n")
            print("""
           |
     \     |     /
       \       /
         ,d8b,      
 - --- - 88888 --- - 
         '98P'      
       /       \    
     /     |     \\
           |
                """)
            print("\n" * 3)
            print('[START]', '🏁🎉!', *partenza, '[GOAL]')
            print("""
                  
BBBB  AAAA  N   N  GGGGG   MM MM
B  B  A  A  NN  N  G       MM MM
BBB   AAAA  N N N  G  GG   MM MM
B  B  A  A  N  NN  G   G  
BBBB  A  A  N   N  GGGGG   MM MM
                  """)
            
            print(*terreno, sep= ".")
            print('\n' * 4)
            time.sleep(1)

            giocata += 1
            secondi += 1
            iterazionitot += 20

        time.sleep(0.1)
        os.system('clear')

        if iterazionitot%100 == 0:

            meteo = not meteo
            gestionemeteo += 1

        if secondi == 60:

            minuti += 1
            secondi = 0

        pista: list[str] = ['_'] * 70

        if decimosecondo == 10:

            if meteo == True:

                pos_t = -1
                pos_l = -2

            else:

                pos_t = 0
                pos_l = 0

            pos_t += tartaruga()
            pos_l += lepre()
            
            posizione_tartaruga += pos_t
            posizione_lepre += pos_l
            decimosecondo = 0

        decimosecondo += 1

        max_tarta: int = posizione_tartaruga
        max_lepre: int = posizione_lepre

        if posizione_tartaruga < 1:

            posizione_tartaruga = 1

            if posizione_lepre < 1:

                posizione_lepre = 1

            elif posizione_lepre >= 70:

                posizione_lepre = 70
                controllo = True

        if posizione_lepre < 1:

            posizione_lepre = 1

            if posizione_tartaruga < 1:

                posizione_tartaruga = 1

            elif posizione_tartaruga >= 70:

                posizione_tartaruga = 70
                controllo == True

        if posizione_tartaruga >= 70 and posizione_lepre >= 70:

            posizione_tartaruga = 70
            posizione_lepre = 70
            controllo = True

        if posizione_tartaruga >= 70:

            posizione_tartaruga = 70
            controllo = True

        if posizione_lepre >= 70:

            posizione_lepre = 70
            controllo = True

        if posizione_tartaruga != posizione_lepre and posizione_tartaruga <= 70 and posizione_lepre <= 70:

            if pos_t > pos_l:

                pista[posizione_tartaruga - 1] = '..🐢-→'
                pista[posizione_lepre - 1] = '←-🐇..'

            elif pos_t < pos_l:

                pista[posizione_tartaruga - 1] = '←-🐢..'
                pista[posizione_lepre - 1] = '..🐇-→'

            elif pos_t == pos_l:

                pista[posizione_tartaruga - 1] = "〰🐢〰"
                pista[posizione_lepre - 1] = "〰🐇〰"

        if posizione_tartaruga == posizione_lepre and posizione_tartaruga < 70 and posizione_lepre < 70:

            pista[posizione_lepre - 1] = "''🐢💥🐇,,,"

        #print(f"proviamo[decimosecondo]: {decimosecondo}----banana[gestionemeteo]: [{gestionemeteo}]----dieciminuti[iterazionitot]: {iterazionitot}")
        print("!!WHO WILL COME FIRST!!?")
        print('Giocata n', giocata, '|', 'Tarta mossa', pos_t, '|', 'Lepre mossa', pos_l)
        print(f"1° pos [{t if posizione_tartaruga > posizione_lepre else l}]= {posizione_tartaruga if posizione_tartaruga > posizione_lepre else posizione_lepre}")
        print(f"2° pos [{t if posizione_tartaruga < posizione_lepre else l}]= {posizione_tartaruga if posizione_tartaruga < posizione_lepre else posizione_lepre}")
        print(f"Tempo di gara: min 0{minuti}:{(str(0) + str(secondi)) if secondi < 10 else secondi} sec \n")
        if controllo == False:

            if meteo == True:

                    print("""

        _
      _( )_          _      
    _(     )_      _( )_
   (_________)   _(     )_
     \  \  \    (_________)
       \  \       \  \ \\
                    \  \   

                            """)

            if meteo == False:

                    print("""
           |
     \     |     /
       \       /
         ,d8b,      
 - --- - 88888 --- - 
         '98P'      
       /       \    
     /     |     \\
           |
                        """)

            print("\n" * 3)
            print('[START]', *pista, '[GOAL]', "\n")

            if posizione_tartaruga > posizione_lepre:

                print(
f"              \n"
f"              \n"                    
f"              \n"
f"         _    \n"
f"     .-./*)   \n"
f"   _/___\/    \n"
f"     U U      "
                )

            elif posizione_tartaruga < posizione_lepre:

                print("""
       _
      (\\\\
       \||
     __(_";
    /    \\
   ()___)\)_""")                

            else:

                print("""                      
                      
 OOO   U   U   CCCC  H   H  [] []
O   O  U   U  C      H   H  || ||
O   O  U   U  C      HHHHH  [] []
O   O  U   U  C      H   H  
 OOO   UUUUU   CCCC  H   H  [] []""")

        if controllo == True:

            os.system('clear')
            print("""
                   __
                  / \--..____
                   \ \       \-----,,,..
                    \ \       \         \--,,..
                     \ \       \         \  ,'
                      \ \       \         \ ``..
                       \ \       \         \-''
                        \ \       \__,,--'''
                         \ \       \.
                          \ \      ,/
                           \ \__..-
                            \ \\
                             \ \\
                              \ \   
                               \ \\
                                \ \\
                                 \ \\
                                  \ \\
                                   \ \\
                                    \_\            
            """)
            time.sleep(1.5)
            os.system('clear')

            if max_tarta >= 70 and max_lepre >= 70:

                print("IT'S A TIE.")
                print('[Tarta pos]=',posizione_tartaruga,'\n', '[Lepre pos]=', posizione_lepre)
                print("""
DDDD   RRRR   AAAAA  W   W
D   D  R   R  A   A  W   W
D   D  RRRR   AAAAA  W W W
D   D  R  R   A   A  WW WW
DDDD   R   R  A   A  W   W
                  """)

            elif posizione_tartaruga >= 70:

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

            elif posizione_lepre >= 70:

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

            print(f"Risultato finale: {max_tarta if max_tarta > max_lepre else max_lepre} vs {max_tarta if max_tarta < max_lepre else max_lepre}")

            if minuti == 0:

                print(f"Durata gara: {secondi} secondi.")

            elif minuti >= 2:

                if secondi == 1:

                    print(f"Durata gara: {minuti} minuti e {secondi} secondo.")

                elif secondi >= 2:
                    
                    print(f"Durata gara: {minuti} minuti e {secondi} secondi.")

            elif minuti == 1:

                if secondi == 0:

                    print(f"Durata gara: {minuti} minuto.")

                elif secondi == 1:

                    print(f"Durata gara: {minuti} minuto e {secondi} secondo.")

                elif secondi >= 2:

                    print(f"Durata gara: {minuti} minuto e {secondi} secondi.")

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

                controllo = True

        if terreno and giocata > 1 and controllo == False:

            if posizione_tartaruga > posizione_lepre:

                if iterazionitot%5 == 0:

                    terreno.pop(0)
                    terreno.append(random.choice([".", ",", "Y", "YY", ".", ",", ",", "@"]))

                print(*terreno, sep= ".")
                print('\n' * 4)

            elif posizione_tartaruga < posizione_lepre:

                terreno.pop(0)
                
                terreno.append(random.choice([".", ",", "Y", "YY", ".", ".", ",", "@"]))
                
                print(*terreno, sep= ".")
                print('\n' * 4)

            else:

                print(*terreno, sep= ".")
                print('\n' * 4)

        if controllo == True:

            controllo = False
            meteo = False
            giocata = 1
            gestionemeteo = 0
            iterazionitot = 0
            decimosecondo = 1
            posizione_tartaruga = 1
            posizione_lepre = 1
            secondi = 0
            minuti = 0
            interruttore = 1
            time.sleep(2)
    
    print("""
            /  
        _--/   
    Made  ||   
    by         
    Dioni      
    ®2025.     
  ||__         
  /--          
""")

gara(tartaruga(), lepre())

# print("\n", "-"*173, "\n", "-"*173, "\n", "-"*173)