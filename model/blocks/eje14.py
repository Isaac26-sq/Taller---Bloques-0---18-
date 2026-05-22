
#  bloques/eje14.py  ── BLOQUE 14 

class Eje14:

    def ejercicio1(self):
        print("========== EJE1: DESEMPAQUETADO BASICO ==========")

        print("\n---- Tupla original ----")
        tupla = (10, 20, 30, 40)
        print(f"  Tupla: {tupla}")

        print("\n---- Desempaquetando con * ----")
        primera, *mitad, ultima = tupla

        print(f"  primera: {primera}")
        print(f"  mitad:   {mitad}")
        print(f"  ultima:  {ultima}")

    def ejercicio2(self):
        print("========== EJE2: UNPACKING EN FUNCIONES CON * ==========")

        def multiplicar(a, b, c):
            return a * b * c

        lista = [2, 3, 4]

        print("\n---- Lista de argumentos ----")
        print(f"  lista: {lista}")

        print("\n---- Llamando multiplicar(*lista) ----")
        resultado = multiplicar(*lista)

        print(f"  multiplicar({lista[0]}, {lista[1]}, {lista[2]}) = {resultado}")

    def ejercicio3(self):
        print("========== EJE3: COMBINAR DICCIONARIOS CON ** ==========")

        dict1 = {"nombre": "Daniel", "edad": 20}
        dict2 = {"carrera": "Sistemas"}

        print("\n---- Diccionarios originales ----")
        print(f"  dict1: {dict1}")
        print(f"  dict2: {dict2}")

        print("\n---- Combinando con ** ----")
        combinado = {**dict1, **dict2}
        print(f"  combinado: {combinado}")

        print("\n---- Verificando que los originales no cambiaron ----")
        print(f"  dict1: {dict1}")
        print(f"  dict2: {dict2}")

    def ejercicio4(self):
        print("========== EJE4: UNPACKING EN BUCLES ==========")

        coordenadas = [(1, 2), (3, 4), (5, 6), (7, 8)]

        print("\n---- Lista de coordenadas ----")
        print(f"  coordenadas: {coordenadas}")

        print("\n---- Desempaquetando en el bucle ----")
        for x, y in coordenadas:
            print(f"  x={x}, y={y}")

        print("\n---- Desempaquetando con indice usando enumerate ----")
        for i, (x, y) in enumerate(coordenadas):
            print(f"  [{i}] x={x}, y={y}")

    def ejercicio5(self):
        print("========== EJE5: UNPACKING EN RETORNO DE FUNCIONES ==========")

        def datos_persona():
            return "Daniel", 20, "Sistemas"

        print("\n---- Funcion que retorna multiples valores ----")
        print(f"  datos_persona() -> ('Daniel', 20, 'Sistemas')")

        print("\n---- Desempaquetando el retorno ----")
        nombre, edad, carrera = datos_persona()
        print(f"  nombre:  {nombre}")
        print(f"  edad:    {edad}")
        print(f"  carrera: {carrera}")

        print("\n---- Ignorando valores con _ ----")
        nombre, _, carrera = datos_persona()
        print(f"  nombre:  {nombre}")
        print(f"  edad:    (ignorada con _)")
        print(f"  carrera: {carrera}")
