#  bloques/eje7.py  ── BLOQUE 7: FUNCIONES



class Eje7:
    

    def ejercicio1(self):
        print("========== EJE1: FUNCION DOBLE ==========")

        class Funciones:
            @staticmethod
            def doble(n):
                return n * 2

        print("Numero a calcular: 20")
        print(Funciones.doble(20))

    def ejercicio2(self):
        print("========== EJE2: SUMA CON *ARGS ==========")

        class Argumentos:
            @staticmethod
            def args(*args):
                return sum(args)

        print("Elementos a sumar: 20, 10, 10, 10")
        print(Argumentos.args(20, 10, 10, 10))

    def ejercicio3(self):
        print("========== EJE3: FACTORIAL RECURSIVO ==========")

        class Factorial:
            @staticmethod
            def calcular_factorial(x):
                if x == 0:
                    return 1
                return x * Factorial.calcular_factorial(x - 1)

        print("Numero a calcular factorial: 5")
        print(Factorial.calcular_factorial(5))

    def ejercicio4(self):
        class Funciones:
            @staticmethod
            def funcion(n):
                resultado = ""
                for i in range(len(n) - 1, -1, -1):
                    resultado = resultado + n[i]
                return resultado

        print("========== EJE4: INVERTIR STRING CON FOR ==========")
        print("Tu palabara es: Buenas tardes")
        print("Al reves: ", Funciones.funcion("Buenas tardes"))

    def ejercicio5(self):
        print("========== EJE3: FILTRAR PARES ==========")

        class Filtro:
            @staticmethod
            def obtener_pares(lista):
                return list(filter(lambda x: x % 2 == 0, lista))

        numeros = [1, 2, 3, 4, 5, 6]
        print(f"Lista original: {numeros}")
        print("Números pares:", Filtro.obtener_pares(numeros))
