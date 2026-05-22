import sys
import time
from view.consola import (
    gotoxy, ocultar_cursor, mostrar_cursor,
    CYAN, AMARILLO, GRIS, BLANCO, ROJO, RESET
)
from view.borde import Borde


class Menu:
    
    def __init__(self, titulo, opciones, x=2, y=1, ancho=38, alto=18):
        self.titulo   = titulo
        self.opciones = opciones
        self.x        = x
        self.y        = y
        self.ancho    = ancho
        self.alto     = alto

    
    def dibujar_menu(self, dos_columnas=False, mostrar_salir=True,
                     texto_salir="[S] Salir"):
        x, y, ancho, alto = self.x, self.y, self.ancho, self.alto

       
        Borde.dibujar(x, y, ancho, alto)

        
        tx = x + (ancho - len(self.titulo)) // 2
        gotoxy(tx, y + 1)
        print(CYAN + self.titulo + RESET, end="")

        
        gotoxy(x, y + 2)
        print(GRIS + "╠" + "═" * (ancho - 2) + "╣" + RESET, end="")

        
        if self.opciones and self.opciones[0].startswith("__sub__"):
            sub = self.opciones[0].replace("__sub__", "").strip()
            sx = x + (ancho - len(sub)) // 2
            gotoxy(sx, y + 3)
            print(GRIS + sub + RESET, end="")
            lista = self.opciones[1:]
            fila_ini = y + 5
        else:
            lista = self.opciones
            fila_ini = y + 4

       
        if dos_columnas:
            mitad = (len(lista) + 1) // 2
            col_a = lista[:mitad]
            col_b = lista[mitad:]
            ancho_col_a = max((len(op) for op in col_a), default=0)
            ancho_col_b = max((len(op) for op in col_b), default=0)
            sep_columnas = 4
            ancho_bloque = ancho_col_a + sep_columnas + ancho_col_b
            margen = (ancho - ancho_bloque) // 2
            col_izq = x + margen
            col_der = col_izq + ancho_col_a + sep_columnas

            for i, nombre in enumerate(lista):
                if i < mitad:
                    gotoxy(col_izq, fila_ini + i)
                else:
                    gotoxy(col_der, fila_ini + (i - mitad))
                print(AMARILLO + nombre + RESET, end="")
        else:
            ancho_opcion = max((len(op) for op in lista), default=0)
            margen = (ancho - ancho_opcion) // 2
            ox = x + margen
            for i, nombre in enumerate(lista):
                gotoxy(ox, fila_ini + i)
                print(AMARILLO + nombre + RESET, end="")

       
        if mostrar_salir:
            gotoxy(x, y + alto - 3)
            print(GRIS + "╠" + "═" * (ancho - 2) + "╣" + RESET, end="")
            sx = x + (ancho - len(texto_salir)) // 2
            gotoxy(sx, y + alto - 2)
            print(GRIS + texto_salir + RESET, end="")

        sys.stdout.flush()

    def pedir_opcion(self, validas):
        
        py = self.y + self.alto + 1
        px = self.x                       
        prompt = "Opcion: "
        ancho_limpieza = max(self.ancho, 40)

        while True:
            
            gotoxy(px, py)
            print(" " * ancho_limpieza, end="")

            
            gotoxy(px, py)
            print(BLANCO + prompt + RESET, end="")

           
            gotoxy(px + len(prompt), py)
            mostrar_cursor()
            sys.stdout.flush()

            entrada = input().strip().lower()

           
            gotoxy(px, py + 1)
            print(" " * ancho_limpieza, end="")

            if entrada in validas:
                sys.stdout.flush()
                return entrada

           
            ocultar_cursor()
            gotoxy(px, py + 1)
            print(ROJO + "  Ingrese una de las opciones." + RESET, end="")
            sys.stdout.flush()

            time.sleep(1.2)   
            
            gotoxy(px, py + 1)
            print(" " * ancho_limpieza, end="")
            gotoxy(px, py)
            print(" " * ancho_limpieza, end="")
            sys.stdout.flush()
