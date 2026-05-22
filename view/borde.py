import sys
from view.consola import gotoxy


class Borde:
    TL = "╔"; TR = "╗"; BL = "╚"; BR = "╝"
    H  = "═"; V  = "║"

    @staticmethod
    def dibujar(x, y, ancho, alto):
        gotoxy(x, y)
        print(Borde.TL + Borde.H * (ancho - 2) + Borde.TR, end="")

        for fila in range(1, alto - 1):
            gotoxy(x, y + fila)
            print(Borde.V + " " * (ancho - 2) + Borde.V, end="")

        gotoxy(x, y + alto - 1)
        print(Borde.BL + Borde.H * (ancho - 2) + Borde.BR, end="")
        sys.stdout.flush()
