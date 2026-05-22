#  bloques/eje6.py  ── BLOQUE 6: BUCLES (for / while)



class Eje6:
    

    def ejercicio1(self):
        print("========== EJE1: CONTADOR DEL 1 AL 10 ==========")
        cont = 1
        while cont <= 10:
            print(cont)
            cont += 1

    def ejercicio2(self):
        print("========== EJE2: RECORRIDO DE LISTA CON ENUMERATE ==========")
        frutas = ["Pera", "Aguacate", "Manzana", "Fresa", "Guineo"]

        for indice, fruta in enumerate(frutas):
            print(indice, fruta)

    def ejercicio3(self):
        print("========== EJE3: LIST COMPREHENSION ==========")
        Cuadrados = [x**2 for x in range(1, 11) if x % 2 == 0]
        print(Cuadrados)

    def ejercicio4(self):
        class BuclesListas:
            @staticmethod
            def Descuento():
                precios = [100, 60, 40, 30, 70]
                print(f"{'Id':<5} {'Precio original':<18} {'Precio final':<10}")
                print("-" * 40)
                for indice, precio in enumerate(precios):
                    if precio > 50:
                        descuento = precio * 0.10
                        precio_des = precio - descuento
                        print(f"{indice:<5} {precio:<18} {precio_des:<10}")
                    else:
                        print(f"{indice:<5} {precio:<18} {'Sin descuento':<10}")

            @staticmethod
            def list_comprehension():
                numeros = [x for x in range(21) if x % 3 == 0 and x**2 > 50]
                print(numeros)

        
        print("\n------ Descuento del 10% ------")
        BuclesListas.Descuento()
        print("\n------ List Comprehension ------")
        BuclesListas.list_comprehension()
    

    def ejercicio5(self):
        print("-- Crea una lista de 5 nombres y recórrela con un while --")        
        Quintillizas = ["Ichika", "Yotsuba", "Nino", "Mikue", "Itzuki"]
        i = 0
        while i < len(Quintillizas):
            if len(Quintillizas[i]) > 5:
                print(Quintillizas[i], ": Nombre largo")
            else:
                print(Quintillizas[i], ": Nombre corto")
            i += 1