#  bloques/eje2.py  ── BLOQUE 2: VARIABLES Y TIPOS DE DATOS

class Eje2:
    
    def ejercicio1(self):
        print("----- Variables Tipo Simple -----")
        print(f"int = {19}")
        print(f"float = {3.45}")
        print("str = Hola")
        print(f"bool = {False}")
        print(f"Nulo = {None}")
        print("")
        print("----- Variables Complejas -----")
        print(f"Lista - List[Any] = {[4, 5, 1, True, 'Isaac']}")
        print(f"tupla - tuple() = {(1, 'hello', 3.14)}")
        print("diccionario - Dict[str, Any] = ", {"nombre": "Juan", "edad": 25})
        print(f"conjunto = Set[int] = {1, 2, 3, 4, 5}")
        print("")

    def ejercicio2(self):
        Lista = [20, "Hola", 40, "Ingenieria", 60]

        print("--- Imprimir lista [20, Hola, 40, Ingenieria, 60] ---")
        print("Lista[0]: ",Lista[0])
        print("Lista[-1:]: ",Lista[-1:])
        print("Lista[1:4]: ",Lista[1:4])
        print("")

    def ejercicio3(self):
       
    
        print("-- Imprimir Posiciones Especificas")
        caracter = "hola"
        print("Hola | lista = [10, 20, 20, 30] | Dicc: Nombre : Isaac")
        print(caracter[0])
        lista = [10, 20, 20, 30]
        print(lista[-1:])
        diccionario = {"Nombre": "Isaac"}
        print(diccionario["Nombre"])

       

    def ejercicio4(self):
        print("----- Modificar una Posición - Lista[1] -----")
        lista = ["Manzana", "Pera", "Plátano"]
        
        lista[1] = "Uva"
        print("Lista = [Manzana, Pera, Plátano ]")
        print(f"Lista modificada: {lista}")
        print("")

    def ejercicio5(self):
        print("----- Insertar en una Posición - .insert() -----")
        lista = [10, 20, 30]
        lista.insert(0, 5)
        
        print("Lista = [10, 20, 30]")
        print(f"Lista con nuevo elemento: {lista}")
        print("")



