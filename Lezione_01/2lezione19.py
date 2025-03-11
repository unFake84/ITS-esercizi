while True:

    try:

        utente: int = (int(input("Inserire un numero: ")))

        if utente > 0:

            if utente % 2 == 0:

                cont: int = 4
                result: int = 0

                while cont <= utente:

                    result += cont
                    cont += 4

                print(result)

            else:

                cont = 1
                result = 1

                while cont <= utente:

                    result *= cont
                    cont = cont + 2

                print(result)

        else:

            print("Errore.")
            break

    except ValueError:

        print("Non è stato inserito un numero.")