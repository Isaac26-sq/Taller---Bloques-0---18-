
#  bloques/eje11.py  ── BLOQUE 11 


class Eje11:
    

    def ejercicio1(self):
        print("========== EJE1: OPERACIONES CON CONJUNTOS ==========")

        conjunto1 = {1, 2, 3, 4, 5, 6}
        conjunto2 = {1, 3, 4, 6, 7, 8}

        print("\n---- Conjuntos originales ----")
        print(f"  Conjunto 1: {conjunto1}")
        print(f"  Conjunto 2: {conjunto2}")

        print("\n---- Union (|): todos los elementos ----")
        print(f"  Resultado: {conjunto1 | conjunto2}")

        print("\n---- Interseccion (&): los que estan en AMBOS ----")
        print(f"  Resultado: {conjunto1 & conjunto2}")

        print("\n---- Diferencia (-): los del 1 que NO estan en el 2 ----")
        print(f"  Resultado: {conjunto1 - conjunto2}")

        print("\n---- Diferencia simetrica (^): los que NO se repiten ----")
        print(f"  Resultado: {conjunto1 ^ conjunto2}")


    def ejercicio2(self):
        print("========== EJE2: ELIMINAR DUPLICADOS CON SET ==========")

        duplicados = [1, 2, 2, 3, 3, 3, 4]

        print("\n---- Lista original ----")
        print(f"  {duplicados}")

        print("\n---- Lista sin duplicados (convertida a set) ----")
        print(f"  {set(duplicados)}")


    def ejercicio3(self):
        print("========== EJE3: ELEMENTOS UNICOS (no compartidos) ==========")

        conjunto1 = {1, 2, 3, 4, 5, 6}
        conjunto2 = {1, 3, 4, 6, 7, 8}

        print("\n---- Conjuntos originales ----")
        print(f"  Conjunto 1: {conjunto1}")
        print(f"  Conjunto 2: {conjunto2}")

        union        = conjunto1 | conjunto2
        interseccion = conjunto1 & conjunto2
        resultado    = union - interseccion

        print("\n---- Paso a paso ----")
        print(f"  Union (todos):        {union}")
        print(f"  Interseccion (comun): {interseccion}")
        print(f"  Union - Interseccion: {resultado}")

        print("\n---- Conclusion ----")
        print(f"  Elementos que estan en uno pero NO en el otro: {resultado}")

    def ejercicio4(self):
        print("========== EJE4: ESTUDIANTES Y MATERIAS ==========")

        matematicas = {"Ana", "Luis", "Pedro", "Maria", "Carlos"}
        fisica      = {"Luis", "Maria", "Sofia", "Carlos", "Diego"}

        print("\n---- Aprobados por materia ----")
        print(f"  Matematicas: {matematicas}")
        print(f"  Fisica:      {fisica}")

        print("\n---- Aprobaron AMBAS materias ----")
        print(f"  {matematicas & fisica}")

        print("\n---- Aprobaron SOLO matematicas ----")
        print(f"  {matematicas - fisica}")

        print("\n---- Aprobaron SOLO fisica ----")
        print(f"  {fisica - matematicas}")

        print("\n---- Aprobaron al menos UNA materia ----")
        print(f"  {matematicas | fisica}")

        print("\n---- Aprobaron solo UNA (no las dos) ----")
        print(f"  {matematicas ^ fisica}")

    def ejercicio5(self):
        
        print("========== EJE5: METODOS DE CONJUNTOS ==========")

        frutas = {"manzana", "pera", "uva"}

        print("\n---- Conjunto inicial ----")
        print(f"  {frutas}")

      
        print("\n---- Agregando 'banana' con .add() ----")
        frutas.add("banana")
        print(f"  {frutas}")

        print("\n---- Intentando agregar 'manzana' otra vez ----")
        frutas.add("manzana")
        print(f"  {frutas}  <- no se duplica :)")

        
        print("\n---- Quitando 'pera' con .remove() ----")
        frutas.remove("pera")
        print(f"  {frutas}")

        
        print("\n---- Verificando con 'in' ----")
        print(f"  ¿'uva' esta en el conjunto?    -> {'uva' in frutas}")
        print(f"  ¿'sandia' esta en el conjunto? -> {'sandia' in frutas}")

        
        print("\n---- Cantidad de elementos ----")
        print(f"  Total de frutas: {len(frutas)}")
    

    


