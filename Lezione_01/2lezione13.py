while True:

    try:

        user_x = int(input("Inserire X: "))
        user_y = int(input("Inserire Y: "))
        user_z = int(input("Inserire Z: "))

        if user_x > 0 and user_y > 0 and user_z > 0:

            break

        else:

            print("Uno o più numeri sono negativi, riprovare.")
    
    except ValueError:

        print("Hai erroneamente inserito un non numero.")

print(f"Hai inserito [x]{user_x} - [y]{user_y} - [y]{user_z}.")


if user_x%2 == 0 and user_y%2 == 0 and user_z%2 == 0 and user_x%3 == 0 and user_y%5 == 0 and user_z%7 == 0:

    print("Regole rispettate.")

else:

    print("regole non rispettate.")