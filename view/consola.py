import os
import sys
import ctypes


kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


CYAN     = "\033[96m"
AMARILLO = "\033[93m"
VERDE    = "\033[92m"
ROJO     = "\033[91m"
BLANCO   = "\033[97m"
GRIS     = "\033[90m"
RESET    = "\033[0m"



try:
    _size = os.get_terminal_size()
    COLS_PANTALLA = _size.columns
    ROWS_PANTALLA = _size.lines
except OSError:
    COLS_PANTALLA = 100
    ROWS_PANTALLA = 32


def gotoxy(x, y):
    print(f"\033[{y};{x}H", end="")

def ocultar_cursor():
    print("\033[?25l", end="")

def mostrar_cursor():
    print("\033[?25h", end="")

def limpiar():
    os.system("cls")

def limpiar_ansi():
   
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()



def centrar_x(ancho):
    return (COLS_PANTALLA - ancho) // 2 + 1
