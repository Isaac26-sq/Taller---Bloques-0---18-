
#  bloques/eje15.py  ── BLOQUE 15 

from functools import reduce

class Eje15:

    def ejercicio1(self):
        print("========== EJE1: MAP() - INCREMENTAR ELEMENTOS ==========")

        lista = [2, 4, 6]

        print("\n---- Lista original ----")
        print(f"  lista: {lista}")

        print("\n---- Aplicando map(lambda x: x + 1, lista) ----")
        resultado = list(map(lambda x: x + 1, lista))
        print(f"  resultado: {resultado}")

    def ejercicio2(self):
        print("========== EJE2: FILTER() - FILTRAR MAYORES A 3 ==========")

        lista = [1, 2, 3, 4, 5]

        print("\n---- Lista original ----")
        print(f"  lista: {lista}")

        print("\n---- Aplicando filter(lambda x: x > 3, lista) ----")
        resultado = list(filter(lambda x: x > 3, lista))
        print(f"  resultado: {resultado}")

    def ejercicio3(self):
        print("========== EJE3: REDUCE() - MULTIPLICAR TODOS ==========")

        lista = [1, 2, 3, 4]

        print("\n---- Lista original ----")
        print(f"  lista: {lista}")

        print("\n---- Proceso de reduce(lambda x, y: x * y, lista) ----")
        print(f"  1 * 2 = 2")
        print(f"  2 * 3 = 6")
        print(f"  6 * 4 = 24")

        resultado = reduce(lambda x, y: x * y, lista)
        print(f"\n---- Resultado ----")
        print(f"  resultado: {resultado}")

    def ejercicio4(self):
        print("========== EJE4: COMBINANDO MAP() Y FILTER() ==========")

        lista = [1, 2, 3, 4, 5, 6]

        print("\n---- Lista original ----")
        print(f"  lista: {lista}")

        print("\n---- Filtrando pares con filter() ----")
        pares = list(filter(lambda x: x % 2 == 0, lista))
        print(f"  pares: {pares}")

        print("\n---- Elevando al cuadrado con map() ----")
        resultado = list(map(lambda x: x ** 2, pares))
        print(f"  resultado: {resultado}")

    def ejercicio5(self):
        print("========== EJE5: FUNCION DE ORDEN SUPERIOR PROPIA ==========")

        def aplicar(funcion, lista):
            return [funcion(x) for x in lista]

        lista = [1, 2, 3, 4, 5]

        print("\n---- Lista original ----")
        print(f"  lista: {lista}")

        print("\n---- Pasando lambda como argumento ----")
        triples = aplicar(lambda x: x * 3, lista)
        print(f"  x * 3 -> {triples}")

        negativos = aplicar(lambda x: -x, lista)
        print(f"  -x    -> {negativos}")

        cuadrados = aplicar(lambda x: x ** 2, lista)
        print(f"  x**2  -> {cuadrados}")