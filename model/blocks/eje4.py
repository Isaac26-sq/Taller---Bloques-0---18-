from view.entrada import pedir_varios


class Eje4:

    def ejercicio1(self):
        def validar_nombre(v):
            sin_espacios = v.replace(" ", "")
            if sin_espacios == "" or not sin_espacios.isalpha():
                raise ValueError("invalido")
            if len(sin_espacios) < 2:
                raise ValueError("invalido")
            return v

        def validar_edad(v):
            if not v.isdigit() or int(v) <= 0:
                raise ValueError("invalido")
            return int(v)

       
        nombre, edad = pedir_varios(
            [
                {"etiqueta": "Ingrese su nombre: ", "validador": validar_nombre,
                 "mensaje_error": "Nombre invalido"},
                {"etiqueta": "Ingrese su edad: ", "validador": validar_edad,
                 "mensaje_error": "Ingrese un valor valido"},
            ],
            contexto="MENSAJE PERSONALIZADO",
        )
        print(f"\nMi nombre es {nombre} y tengo {edad} años")

    def ejercicio2(self):
        class Calcular:
            @staticmethod
            def calcula_suma_promedio():
                def validar_entero(v):
                    return int(v)

               
                num1, num2 = pedir_varios(
                    [
                        {"etiqueta": "Ingrese su primer numero: ", "validador": validar_entero,
                         "mensaje_error": "Solo numeros enteros"},
                        {"etiqueta": "Ingrese su segundo numero: ", "validador": validar_entero,
                         "mensaje_error": "Solo numeros enteros"},
                    ],
                    contexto="SUMA Y PROMEDIO",
                )

                suma = num1 + num2
                promedio = suma / 2
                print("\nSuma total de su notas: ", suma)
                print("Su promedio es de: ", promedio)

        Calcular.calcula_suma_promedio()

    def ejercicio3(self):
        print("========== EJE3: CONCATENACION DE STRINGS ==========")
        num = input("Ingrese un valor: ")
        print(num + "5")

    def ejercicio4(self):
        def validar_letras(v):
            sin_espacios = v.replace(" ", "")
            if not sin_espacios.isalpha():
                raise ValueError("invalido")
            if len(sin_espacios) < 2:
                raise ValueError("invalido")
            return v

        nombre, ciudad, comida_fav = pedir_varios(
            [
                {"etiqueta": "Ingrese su nombre: ", "validador": validar_letras,
                 "mensaje_error": "Nombre invalido"},
                {"etiqueta": "Ingrese su ciudad: ", "validador": validar_letras,
                 "mensaje_error": "Solo se permiten letras"},
                {"etiqueta": "Ingrese su comida favorita: ", "validador": validar_letras,
                 "mensaje_error": "Solo se permiten letras"},
            ],
            contexto="DATOS PERSONALES",
        )
       
        print(f"\nMi nombre es {nombre}, vivo en {ciudad} y mi comida favorita es {comida_fav}")

    def ejercicio5(self):
        def validar_entero(v):
            return int(v)

        num1, num2, num3 = pedir_varios(
            [
                {"etiqueta": "Ingrese su primer numero: ", "validador": validar_entero,
                 "mensaje_error": "Solo numeros enteros"},
                {"etiqueta": "Ingrese su segundo numero: ", "validador": validar_entero,
                 "mensaje_error": "Solo numeros enteros"},
                {"etiqueta": "Ingrese su tercer numero: ", "validador": validar_entero,
                 "mensaje_error": "Solo numeros enteros"},
            ],
            contexto="CALCULO DE NOTAS",
        )

        suma = num1 + num2 + num3
        promedio = suma / 3
        print(f"\nNota1: {num1} | Nota2: {num2} | Nota3: {num3}")
        print(f"La suma de su notas son: {suma} | Promedio: {promedio}")

        print("\n------ Concatenacion vs Suma ------")
        def validar_str_numerico(v):
            int(v)
            return v

        num1, num2 = pedir_varios(
            [
                {"etiqueta": "Ingrese su primer numero: ", "validador": validar_str_numerico,
                 "mensaje_error": "Solo numeros"},
                {"etiqueta": "Ingrese su segundo numero: ", "validador": validar_str_numerico,
                 "mensaje_error": "Solo numeros"},
            ],
            contexto="CONCATENACION VS SUMA",
        )
        print("\nConcatenacion: ", num1 + num2)
        print("Suma: ", int(num1) + int(num2))
