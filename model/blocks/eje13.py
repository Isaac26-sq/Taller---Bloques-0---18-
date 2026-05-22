
#  bloques/eje13.py  ── BLOQUE 13 
import time 

class Eje13:
   
    def ejercicio1(self):
        print("========== EJE1: DECORADORES ==========")
        
        def decorador_saludo(funcion):
            def wrapper(*args, **kwargs):
                print("Iniciando función...")
                r = funcion(*args, **kwargs)
                print("Finalizando función...")
            return wrapper

        @decorador_saludo
        def saludo(n):
            print(f"Buenas tardes {n}, ¿Cómo te encuetras?")
        
        saludo("Isaac")

    def ejercicio2(self): 
        print("========== EJE2: DECORADOR VERIFICAR POSITIVO ==========")
        
        def verificar_positivo(funcion):
            def wrapper():
                print("\n---- Validacion de numero ----")
                a = int(input("Ingrese un número: ",validador=lambda x: int(x),mensaje_error="Solo se permiten numeros enteros"))

                if a >= 0: 
                    return funcion(a)
                else: 
                    print("\n---- Validacion fallida ----")
                    print(f"  El número {a} NO es positivo")
            return wrapper  
        
        @verificar_positivo
        def positivos(n):
            print("\n---- Funcion ejecutada ----")
            print(f"  El número {n} es positivo ")
        positivos()

    def ejercicio3(self):
        print("========== EJE3: DECORADOR LOG ==========")

        def log(funcion):
            def wrapper(*args, **kwargs):
                print("\n---- Iniciando operacion ----")
                print(f"  Llamando funcion con argumentos: {args}")
                r = funcion(*args, **kwargs)
                print("\n---- Operacion finalizada ----")
                print(f"  Resultado: {r}")
                return r
            return wrapper

        @log
        def suma(a, b):
            return a + b

        print(f"\n---- Ejecutando suma ----")
        suma(2, 3)

    def ejercicio4(self):
        print("========== EJE4: DECORADOR CRONÓMETRO ==========")

        def cronometro(funcion):
            def wrapper(*args, **kwargs):
                print("Iniciando función...")
                inicio = time.time()
                funcion(*args, **kwargs)
                final = time.time()
                print(f"Tiempo de ejecución: {round(final - inicio, 6)} segundos")
                print("Finalizando función...")
            return wrapper

        @cronometro
        def resta(a, b):
            print(f"Operación: {a} - {b} = {a - b}")
            return a - b

        resta(1000, 200)

    
    def ejercicio5(self):
        print("========== EJE5: DECORADOR MAYÚSCULAS ==========")

        def mayuscula(funcion):
            def wrapper(*args, **kwargs):
                print("Iniciando función...")
                resultado = funcion(*args, **kwargs).upper()
                print(resultado)
                print("Finalizando función...")
            return wrapper

        @mayuscula
        def saludo(n):
            return f"buenos dias {n}, es un placer saludarlo."

        saludo('isaac')

    def ejercicio(self):
         def validar_edad(funcion):
            def wrapper():
                edad = int(input("Ingrese su edad: ", validador= lambda x: int(x), mensaje_error="Solo se permiten numeros enteros" )) 
                if 0 <= edad <=  120:
                    funcion(edad)
                    if edad >= 18: 
                        print("Eres mayor de Edad")
                    else: print("Eres menor de Edad")
                else: print("Edad invalida.")
            return wrapper
         
         @validar_edad
         def edad():
             print("Eres mayor o menor de edad?")
         edad()

             



        



    






