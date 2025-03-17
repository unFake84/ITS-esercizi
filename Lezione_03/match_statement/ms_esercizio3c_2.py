print("-----------------------------------------------------------------------")
print("Benvenuti,\nIn questo programma convertiamo un voto di laurea italiano\nnel sistema GPA americano.")
print("-----------------------------------------------------------------------")
voto_laurea: int = (int(input("Inserire un voto laurea: ")))

match voto_laurea:

    case n if n >= 106 and n <=110:

        print("GPA = 4.0")
        print("-----------------------------------------------------------------------")

    case n if n >= 101 and n <=105:

        print("GPA = 3,7")

    case n if n >= 96 and n <= 100:

        print("GPA = 3.3")

    case n if n >= 91 and n <= 95:

        print("GPA = 3.0")

    case n if n >= 86 and n <= 90:

        print("GPA = 2.7")

    case n if n >= 81 and n <= 85:

        print("GPA = 2.3")

    case n if n >= 76 and n <= 80:

        print("GPA = 2.0")

    case n if n >= 70 and n <= 75:

        print("GPA = 1.7")

    case n if n >= 66 and n <= 69:

        print("GPA = 1.0")

    case _:

        print("Voto non valido!")