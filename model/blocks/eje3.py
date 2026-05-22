#  bloques/eje3.py  ── BLOQUE 3: OPERADORES Y EXPRESIONES

class Eje3:


    def ejercicio1(self):
        class Operadores:
            @staticmethod
            def realizar_operaciones(a, b):
                print("====== OPERACIONES ARITMETICAS ======")
                suma = a + b
                print("Suma =", suma)
                resta = a - b
                print("resta =", resta)
                multiplicar = a * b
                print("multiplicar =", multiplicar)
                division = a / b
                print("division =", division)

        Operadores.realizar_operaciones(20, 4)

    def ejercicio2(self):
        a = [1, 2]
        b = [1, 2]

        print("========== EJE2: VERDADERO Y FALSO ==========")
        print("")
        print("a = [1, 2]")
        print("b = [1, 2]")
        print("a == b: ", a == b)
        print("a is b: ", a is b)

    def ejercicio3(self):
        x = 2 + 1 * 2 % 2 + (2**1) // 2
        print("========== EJE3: ORDEN DE EVALUACION ==========")
        print("Expresion: 2 + 1 * 2 % 2 + (2**1)//2")
        print("R =", x)

    def ejercicio4(self):
        class OperadoresExpresiones:
            @staticmethod
            def Calcular(a, b):
                division = a / b
                print("division =", division)
                modulo = a % b
                print("Modulo =", modulo)
                potencia = a ** b
                print("Potencia =", potencia)
                r = a * b - a // b + b
                print("Resultado: ", r)

            @staticmethod
            def validar():
                a = [1, 2]
                b = a
                print("a = [1, 2]")
                print("b = a")
                print("a == b: ", a == b)
                print("a is b: ", a is b)

            @staticmethod
            def orden():
                x = 3 ** 2 // 4 + 2 * 3 % 5
                print("Expresion: 3 ** 2 // 4 + 2 * 3 % 5")
                print("orden : **  --> * --> // --> % --> +")
                print("R: ", x)

        print("--- Operadores Aritmeticos ---")
        OperadoresExpresiones.Calcular(15, 3)
        print("\n--- Validacion == vs is ---")
        OperadoresExpresiones.validar()
        print("\n--- Orden de Evaluacion ---")
        OperadoresExpresiones.orden()

    def ejercicio5(self):
        a = [10, 20]
        c = a  

        print("========== EJE4: REFRENCIA EN MEMORIA ==========")
        print("a = [10, 20]")
        print("c = a")
        
        
        c[0] = 99

        print("c[0] = 99")
        print("¿a es igual a c? (a == c):", a == c)
        print("¿a y c comparten la misma identidad? (a is c):", a is c)
        print("Lista final de a:", a)  
