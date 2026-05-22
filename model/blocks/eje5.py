from view.entrada import pedir_varios


class Eje5:

    def ejercicio1(self):
        print("============= PAR E IMPAR =============")

        def validar_entero(v):
            return int(v)

        num = input("Ingrese un numero: ", validador=validar_entero, mensaje_error="Solo se permiten numeros enteros")

        if num < 0:
            print("Numero invalido")
        elif num % 2 == 0:
            print(f"Numero {num}:  es par")
        else:
            print(f"Numero {num}:  es impar")

    def ejercicio2(self):
        print("============= CALIFICACION LETRA =============")

        def validar_nota(v):
            n = int(v)
            if n < 0 or n > 10:
                raise ValueError("invalido")
            return n

        num = input("Ingrese una nota (0 - 10): ", validador=validar_nota, mensaje_error="Ingrese un numero entre 0 y 10")

        if num == 10:
            print("Su calificacion es: A")
        elif num == 9:
            print("Su calificacion es: B")
        elif num == 8:
            print("Su calificacion es: C")
        else:
            print("Su calificacion es: D")

    def ejercicio3(self):
        class SistemaLogin:
            @staticmethod
            def login():
                
                usuario, password = pedir_varios(
                    [
                        {"etiqueta": "Ingrese su usuario: ", "validador": None,
                         "mensaje_error": "Campo vacio"},
                        {"etiqueta": "Ingrese su contraseña: ", "validador": None,
                         "mensaje_error": "Campo vacio"},
                    ],
                    contexto="SISTEMA DE LOGIN",
                )

                if usuario == "admin" and password == "123":
                    print("Bienvenido!")
                else:
                    print("Acceso denegado!")

        SistemaLogin.login()

    def ejercicio4(self):
        class CondicionesValidaciones:
            @staticmethod
            def Solicitar():
                def validar_entero(v):
                    return int(v)

                num = input("Ingrese un numero: ", validador=validar_entero, mensaje_error="Solo se permiten numeros enteros")

                if num == 0:
                    print("Su numero es cero")
                elif num < 0:
                    print("Su numero es negativo")
                else:
                    print("Su numero es positivo")
                    if num > 100:
                        print("Y es mayor a 100")
                    elif num < 100:
                        print("Y es menor a 100")
                    else:
                        print("Y es exactamente 100")

            @staticmethod
            def temp():
                def validar_entero(v):
                    return int(v)

                temperatura = input("Ingrese una temperatura: ", validador=validar_entero, mensaje_error="Solo se permiten numeros enteros")

                if temperatura < 0:
                    print("Hace mucho frio")
                elif temperatura < 15:
                    print("Hace frio")
                elif temperatura < 25:
                    print("Temperatura agradable")
                elif temperatura < 35:
                    print("Hace calor")
                else:
                    print("Hace mucho calor")

            @staticmethod
            def cajero_automatico():

                saldo = 1000
                intentos = {"n": 0}
                BLOQUEADO = -1

                def validar_pin(v):
                    n = int(v)
                    if n == 1234:
                        return n
                    intentos["n"] += 1
                    if intentos["n"] >= 3:
                        return BLOQUEADO
                    raise ValueError("PIN invalido")
                def validar_monto(v):
                    n = int(v)
                    if n < 0:
                        raise ValueError("Cantidad invalida")
                    if n > saldo:
                        raise ValueError("Saldo insuficiente")
                    return n

                pin = input("Ingrese su PIN: ", validador=validar_pin, mensaje_error="PIN invalido")

                if pin == BLOQUEADO:
                    print("Cuenta bloqueada, muchos intentos")
                    return

                monto = input("Ingrese un monto a retirar: ", validador=validar_monto, mensaje_error=f"Ingrese un monto entre 0 y {saldo}")

                restante = saldo - monto
                print(f"Retira: {monto}")
                print(f"Saldo anterior: {saldo}")
                print(f"Saldo actual: {restante}")

        print("--- 1. NUMERO POSITIVO, NEGATIVO O CERO ---")
        CondicionesValidaciones.Solicitar()
        print("\n--- 2. TEMPERATURA ---")
        CondicionesValidaciones.temp()
        print("\n--- 3. CAJERO AUTOMATICO - RETIRAR ---")
        CondicionesValidaciones.cajero_automatico()

    def ejercicio5(self):
        class SistemaLogin:
            @staticmethod
            def login():
                USUARIO_OK = "admin"
                PASSWORD_OK = "123"

                intentos = {"n": 0}

                def validar_letras(v):
                    if not v.replace(" ", "").isalpha():
                        raise ValueError("Solo se permiten letras")
                    return v

                def validar_usuario(v):
                    validar_letras(v)
                    if v != USUARIO_OK:
                        intentos["n"] += 1
                        restantes = 3 - intentos["n"]
                        if restantes <= 0:
                            raise ValueError("Cuenta bloqueada")
                        raise ValueError(f"Usuario incorrecto. Intentos: {restantes}")
                    return v

                def validar_password(v):
                    if v != PASSWORD_OK:
                        intentos["n"] += 1
                        restantes = 3 - intentos["n"]
                        if restantes <= 0:
                            raise ValueError("Cuenta bloqueada")
                        raise ValueError(f"Contraseña incorrecta. Intentos: {restantes}")
                    return v

                
                usuario, password = pedir_varios(
                    [
                        {"etiqueta": "Ingrese su usuario: ", "validador": validar_usuario,
                         "mensaje_error": "Usuario incorrecto"},
                        {"etiqueta": "Ingrese su contraseña: ", "validador": validar_password,
                         "mensaje_error": "Contraseña incorrecta"},
                    ],
                    contexto="LOGIN CON VALIDACION",
                )

                print("Bienvenido!")

        SistemaLogin.login()
