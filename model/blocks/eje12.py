
#  bloques/eje12.py  ── BLOQUE 12 



class Eje12:

    def ejercicio1(self):
        print("========== EJE1: CAPTURAR ValueError ==========")

        print("\n---- Conversion de texto a numero ----")
       
        try:
            
            entrada = input("  Ingresa un numero entero: ")
            n = int(entrada)

            print("\n---- Conversion exitosa ----")
            print(f"  El numero ingresado es: {n}")
            print(f"  Su doble es: {n * 2}")

        except ValueError as e:
            print("\n---- Error capturado ----")
            print(f"  Tipo de error: ValueError")
            print(f"  Mensaje: {e}")
            print(f"  Eso no era un numero valido..")

    def ejercicio2(self):
        print("========== EJE2: CAPTURAR IndexError ==========")

        lista = [1, 2, 3]

        print("\n---- Lista original ----")
        print(f"  Lista: {lista}")
        print(f"  Tamaño: {len(lista)} elementos (indices 0, 1, 2)")

        print("\n---- Intentando acceder a lista[5] ----")
        try:
            print(f"  Valor en posicion 5: {lista[5]}")

        except IndexError as e:
            print("\n---- Error capturado ----")
            print(f"  Tipo de error: IndexError")
            print(f"  Mensaje: {e}")
            print(f"  Esa posicion no existe en la lista...")



    def ejercicio3(self):
        print("========== EJE3: MANEJO DE MULTIPLES ERRORES ==========")

        print("\n---- Division de dos numeros ----")
        try:
            n  = int(input("  Ingrese un número: "))
            n1 = int(input("  Ingrese otro número: "))

            resultado = n / n1

            print("\n---- Division exitosa ----")
            print(f"  {n} / {n1} = {round(resultado, 2)}")

        except ValueError as e:
            print("\n---- Error capturado ----")
            print(f"  Tipo de error: ValueError")
            print(f"  Mensaje: {e}")
            print(f"  Numero invalido...")

        except ZeroDivisionError as e:
            print("\n---- Error capturado ----")
            print(f"  Tipo de error: ZeroDivisionError")
            print(f"  Mensaje: {e}")
            print(f"  No se puede dividir para cero...")


    def ejercicio4(self):

        print("========== EJE4: TRY / EXCEPT / ELSE / FINALLY ==========")

        print("\n---- Calculo de raiz cuadrada ----")
        try:
            n = int(input("  Ingrese un número positivo: "))
            raiz = n ** 0.5

        except ValueError as e:
            print("\n---- Error capturado ----")
            print(f"  Tipo de error: ValueError")
            print(f"  Mensaje: {e}")
            print(f"  Numero invalido...")

        else:
            print("\n---- Calculo exitoso (else) ----")
            print(f"  La raiz cuadrada de {n} es: {round(raiz, 2)}")

        finally:
            print("\n---- Bloque finally ----")
            print(f"  Esto se ejecuta SIEMPRE (haya error o no)")


    def ejercicio5(self):
        print("========== EJE5: LANZAR ERRORES CON RAISE ==========")

        print("\n---- Validacion de edad ----")
        try:
            edad = int(input("  Ingrese su edad: "))

            if edad < 0:
                raise ValueError("La edad no puede ser negativa")
            if edad > 120:
                raise ValueError("La edad no puede ser mayor a 120")

            print("\n---- Edad valida ----")
            print(f"  Tu edad es: {edad} años")

        except ValueError as e:
            print("\n---- Error capturado ----")
            print(f"  Tipo de error: ValueError")
            print(f"  Mensaje: {e}")
            print(f"  Por favor ingrese una edad valida...")

        

            

    
        
