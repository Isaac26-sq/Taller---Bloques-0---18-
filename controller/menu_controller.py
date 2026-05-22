import sys
import importlib

from view.menu import Menu
from view.ejercicio_box import EjercicioBox
from view.etiquetas import nombre_bloque, descripcion_ejercicio
from view.consola import (
    gotoxy, limpiar, ocultar_cursor, mostrar_cursor,
    centrar_x,
    CYAN, BLANCO, ROJO, RESET,
    
)


class MenuController:

    NUM_BLOQUES    = 20   
    NUM_EJERCICIOS = 5

    MP_ANCHO = 81
    MP_ALTO  = 19 

    SB_ANCHO = 60
    SB_ALTO  = 15

   
    EJ_ANCHO = 86
    EJ_ALTO  = 28

   
    GAP = 3

    def __init__(self):
        self.bloques_nombres = [nombre_bloque(i) for i in range(self.NUM_BLOQUES)]

        ancho_total = self.MP_ANCHO + self.GAP + self.SB_ANCHO
        x_inicial = centrar_x(ancho_total)

        self.MP_X = x_inicial
        self.MP_Y = 2

        self.SB_X = x_inicial + self.MP_ANCHO + self.GAP
        self.SB_Y = 2

    
    def _crear_menu_principal(self):
        opciones = [f"__sub__Elige un bloque (0-{self.NUM_BLOQUES - 1})"]
        for i, nombre in enumerate(self.bloques_nombres):
            opciones.append(f"[{i:>2}] {nombre}")
        return Menu(
            titulo="★  MENU PRINCIPAL  ★",
            opciones=opciones,
            x=self.MP_X, y=self.MP_Y,
            ancho=self.MP_ANCHO, alto=self.MP_ALTO
        )

    
    def _dibujar_menu_principal(self):
        menu = self._crear_menu_principal()
        menu.dibujar_menu(dos_columnas=True, texto_salir="[S] Salir")
        return menu

   
    def mostrar_menu_principal(self):
        validas = ["s"] + [str(i) for i in range(self.NUM_BLOQUES)]

        while True:
            limpiar()
            ocultar_cursor()
            menu = self._dibujar_menu_principal()

            entrada = menu.pedir_opcion(validas)

            if entrada == "s":
                limpiar()
                print(CYAN + "Hasta luego!" + RESET)
                break
            else:
                
                self.mostrar_submenu_bloque(int(entrada))

   
    def _dibujar_prompt_principal(self, num_bloque):
        py = self.MP_Y + self.MP_ALTO + 1
        px = self.MP_X
        texto = f"Opcion: {num_bloque}"
        gotoxy(px, py)
        print(" " * max(self.MP_ANCHO, 40), end="")
        gotoxy(px, py)
        print(BLANCO + texto + RESET, end="")
        sys.stdout.flush()

    def mostrar_submenu_bloque(self, num_bloque):
        opciones = ["__sub__Elige un ejercicio"]
        for i in range(1, self.NUM_EJERCICIOS + 1):
            desc = descripcion_ejercicio(num_bloque, i)
            opciones.append(f"[{i}] Ejercicio {i}  |  {desc}")

        submenu = Menu(
            titulo=nombre_bloque(num_bloque),
            opciones=opciones,
            x=self.SB_X, y=self.SB_Y,
            ancho=self.SB_ANCHO, alto=self.SB_ALTO
        )

        validas = ["0"] + [str(i) for i in range(1, self.NUM_EJERCICIOS + 1)]

        limpiar()
        ocultar_cursor()
        self._dibujar_menu_principal()
        self._dibujar_prompt_principal(num_bloque)
        submenu.dibujar_menu(dos_columnas=False, texto_salir="[0] Volver")

        while True:
            entrada = submenu.pedir_opcion(validas)

            if entrada == "0":
                break
            else:
                self.ejecutar_ejercicio(num_bloque, int(entrada))
                limpiar()
                ocultar_cursor()
                self._dibujar_menu_principal()
                self._dibujar_prompt_principal(num_bloque)
                submenu.dibujar_menu(dos_columnas=False, texto_salir="[0] Volver")

   
    def ejecutar_ejercicio(self, num_bloque, num_ejercicio):
        desc = descripcion_ejercicio(num_bloque, num_ejercicio)
        caja = EjercicioBox(
            titulo=f"[ {nombre_bloque(num_bloque)}  -  "
                   f"Ejercicio {num_ejercicio}: {desc} ]"
        )

        try:
            modulo = importlib.import_module(f"model.blocks.eje{num_bloque}")
            nombre_clase = f"Eje{num_bloque}"
            clase = getattr(modulo, nombre_clase)
            instancia = clase()

            nombre_metodo = f"ejercicio{num_ejercicio}"
            if hasattr(instancia, nombre_metodo):
                metodo = getattr(instancia, nombre_metodo)
                caja.ejecutar_funcion(metodo)
            else:
                caja.dibujar()
                caja.imprimir(f"'{nombre_metodo}' no esta implementado.", color=ROJO)
        except ModuleNotFoundError:
            caja.dibujar()
            caja.imprimir(f"No se encontro model/blocks/eje{num_bloque}.py", color=ROJO)
        except Exception as e:
            caja.dibujar()
            caja.imprimir(f"Error: {e}", color=ROJO)

        caja.esperar_tecla()
