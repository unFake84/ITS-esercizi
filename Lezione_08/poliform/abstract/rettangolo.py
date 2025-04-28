from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    def __init__(self):
        super().__init__()

        self.setShape("rettangolo")

    def draw(self) -> None:

        print(f"\n{self.getShape()}:\n")

        # istruzioni per disegnare un rettangolo 5x10

        # outer for
        for i in range(5):

            # inner for
            for j in range(5*2):

                #lato a e lato d del rettangolo
                if i == 0 or i == 5-1:

                    print("*", end= " ")  # <- end= evita di andare accapo

                # lato b e lato c del rettangolo
                elif j == 0 or j == (5*2) -1:

                    print("*", end=" ")

                # stampare spazio bianco
                else:

                    print(" ", end= " ")

            print("\n", end="")