
while True:
                         
        n:int = int(input("inserire il numero di neonati:\nPremere '0' per uscire:"))

        match n:

            # n=1
            case 1:
                
                print("Congratulazioni!")

            # n=2
            case 2:

                print("Wow! Gemelli!")

            # n=3
            case 3:

                print("Wow! Tre!")

            # n=4
            case 4:

                print("Mamma mia Quattro! Wow!")

            # n=5
            case 5:

                print(f"Incredibile! Cinque!")

            case 0:
                  
                  break


                        
            # default case
            case _:             

                print(f"Non ci credo {n} bambini!")