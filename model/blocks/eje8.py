#  bloques/eje8.py  ── BLOQUE 8: LISTAS

class Eje8:

    def ejercicio1(self):
        print("Crea lista, agrégale 3 elementos con append(), ordénala y muéstrala.")
        print("\nLista = [2, 4, 5]")
        Lista = [2, 4, 5]
        Lista.append(19)
        Lista.append(7)
        Lista.append(20)
        Lista.sort()
        print(Lista)

    def ejercicio2(self):
        lista = [5, 3, 8, 1, 9, 3]
        print("Calcula suma, máximo y mínimo de [5,3,8,1,9,3].")
        print("\nLa suma de su lista: [5,3,8,1,9,3] es = ", sum(lista))
        print("El maximo de su lista: [5,3,8,1,9,3] es = ", max(lista))
        print("El minimo de su lista: [5,3,8,1,9,3] es = ", min(lista))

    def ejercicio3(self):
        lista = [1, 2, 3, 4]
        copia = lista
        copia.append(4)
        print("¿Qué pasa si haces copia=lista 'lista = [5,3,8,1,9,3]' y luego copia.append(4)? ¿Por qué?")
        print("\nIgual se agrega el cuatro dentro de la copia, debido a que la variable")
        print("copia esta guardando la lista")
        print(copia)

    def ejercicio4(self):
        print("========== EJE4: MANIPULACIÓN DE LISTAS ==========")
        print("\n------ Lista inicial ------")
        Estudiantes = ["Isaac", "Kaneki", "Subaru", "Ren", "Anthony"]
        print(Estudiantes)

        print("\n------ Reemplazar ultimo estudiante ------")
        Estudiantes = ["Isaac", "Kaneki", "Subaru", "Ren", "Anthony"]
        print("Sin append: ", Estudiantes)
        Estudiantes.append("Okarun")
        print("Con append: ", Estudiantes)

        print("\n------ Eliminar primer estudiante ------")
        print("Sin remove(): ", Estudiantes)
        Estudiantes.remove("Isaac")
        print("Con remove()", Estudiantes)

       
    def ejercicio5(self):
        print("========== EJE4: TRUCOS CON TUPLAS ==========")
        
        print("\n1. Intercambio de valores  usando tuplas implícitas")
        x = 10
        y = 50
        print(f"\nAntes del intercambio -> x: {x}, y: {y}")
        
        x, y = y, x 
        print(f"Después del intercambio -> x: {x}, y: {y}")
        print("")

        print("2. Tuplas como llaves de un diccionario (Coordenadas)")
        print("--- Tuplas como llaves de Diccionario ---")
        ubicaciones = {
            (-1.801, -79.534): "Babahoyo",
            (-2.170, -79.922): "Guayaquil"
        }
        
        coordenada = (-1.801, -79.534)
        print(f"\nBuscando coordenada {coordenada}...")
        print(f"Ciudad encontrada: {ubicaciones[coordenada]}")