#  bloques/eje0.py  ── BLOQUE 0: INTRODUCCIÓN A POO

class Eje0:
    
    def ejercicio1(self):
        print("=============== POSIBLES CLASES ===============")
        print("-----------------------------------------------")
        print("libro, prestamo, usuario, autor, editorial, Genero")
        print("-----------------------------------------------")

    def ejercicio2(self):
        class Persona:
            def __init__(self, nombre, edad, genero):
                self.nombre = nombre
                self.edad = edad
                self.genero = genero

            def saludo(self):
                print(f"Buenos dias, {self.nombre}")

        persona1 = Persona("Isaac", 20, "Masculino")
        persona2 = Persona("Carlos", 40, "Masculina")
        persona3 = Persona("Karen", 25, "Femenino")
        print("========== EJE2: INSTANCIAS DE UNA CLASE ==========")
        print("")
        print(persona1.nombre, persona1.edad, persona1.genero)
        persona1.saludo()
        print(persona2.nombre, persona2.edad, persona2.genero)
        persona2.saludo()
        print(persona3.nombre, persona3.edad, persona3.genero)
        persona3.saludo()

    def ejercicio3(self):
        print("========== EJE3: CLASE VS OBJETO ==========")
        print("")
        print("Clase:  Es el molde que va a estructurar a tu objeto o instancia (Plano de casa)")
        print("Objeto: Toma la estructura de la clase para poder existir   (Casa construida)")

    def ejercicio4(self):
        class Telefono:
            def __init__(self, marca, modelo, precio):
                self.marca = marca
                self.modelo = modelo
                self.precio = precio

            def mostrar_info(self):
                print(f"Marca: {self.marca} | Modelo: {self.modelo} | Precio: {self.precio}$")

            def aplicar_descuento(self, porcentaje):
                descuento = self.precio * (porcentaje / 100)
                self.precio = self.precio - descuento
                print(f"Calculando descuento para el {self.marca}...   Descuento aplicado: {descuento} $")
                print(f"Marca: {self.marca} | Modelo: {self.modelo} | Precio: {self.precio} $")

        tele1 = Telefono("Xiaomi", "Note 14 Pro", 500)
        tele2 = Telefono("Poco", "F8 Pro", 700)
        tele3 = Telefono("Iphone", "17 Pro", 1700)
        print("========== EJE4: METODOS Y DESCUENTOS ==========")
        print("")
        print("---- Xiaomi ----")
        tele1.mostrar_info(); tele1.aplicar_descuento(20)
        print("")
        print("---- POCO ----")
        tele2.mostrar_info(); tele2.aplicar_descuento(20)
        print("")
        print("---- Iphone ----")
        tele3.mostrar_info(); tele3.aplicar_descuento(20)

    def ejercicio5(self):
        class CuentaBancaria:
            def __init__(self, titular, saldo):
                self.titular = titular
                self.saldo = saldo

            def mostrar_info(self):
                print(f"Titular: {self.titular} | Saldo: {self.saldo}$")

            def despositar(self, monto):
                aumentar = self.saldo + monto
                self.saldo = aumentar

                if monto < 0:
                    print("Monto invlaido....")
                else:
                    print(f"{self.titular} deposita {monto}$ ...")
                    print(f"Titular: {self.titular} | Saldo: {self.saldo}$")

            def retirar(self, monto):
                retirar = self.saldo - monto
                self.saldo = retirar

                if monto > self.saldo:
                    print("Saldo insuficiente...")
                else:
                    print(f"{self.titular} retira {monto}$ ...")
                    print(f"Titular: {self.titular} | Saldo: {self.saldo}$")

        titular1 = CuentaBancaria("Isaac", 1000)
        titular2 = CuentaBancaria("Maria", 2000)
        print("========== EJE5: CUENTA BANCARIA ==========")
        print("")
        print("----- Banco Solidario ----")
        titular1.mostrar_info()
        titular2.mostrar_info()
        print("")
        print("----- Deposito ----")
        titular1.despositar(3000)
        print("")
        print("----- Retiro ----")
        titular2.retirar(30)
