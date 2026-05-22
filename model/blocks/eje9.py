#  bloques/eje9.py  ── BLOQUE 9: TUPLAS

class Eje9:
   

    def ejercicio1(self):
        print("========== EJE1: INMUTABILIDAD DE TUPLAS ==========")
        tupla = (3, 2, 3, 4)
        try:
            tupla[0] = 10
        except TypeError as e:
            print("Error:", e)
            print("Las tuplas son inmutables, no se pueden modificar.")

    def ejercicio2(self):
        print("========== EJE2: UNPACKING CON *RESTO ==========")
        a, b, *resto = (100, 200, 300, 400, 300, 200, 600)
        print("\na, b, *resto = (100, 200, 300, 400, 300, 200, 600)")
        print("Primero:", a, "| Segundo:", b, "| Resto:", *resto)

    def ejercicio3(self):
        print("========== EJE3: RECORRIDO DE COORDENADAS ==========")
        Coordenadas = [(20, 30), (230, 200)]

        for x, y in Coordenadas:
            print(f"x = {x} , y = {y}")

    def ejercicio4(self):
        print("========== OPERACIONES CON CONJUNTOS ==========")
        conju1 = {1, 2, 3, 4}
        conju2 = {3, 4, 5, 6}

        print("Conjunto 1:", conju1)
        print("Conjunto 2:", conju2)
        print("Elementos en comun:", conju1 & conju2)
        print("Diferencia (en 1 pero no en 2):", conju1 - conju2)
        print("Union:", conju1 | conju2)

        print("\n========== ELIMINAR DUPLICADOS ==========")
        nombres = ["Ana", "Luis", "Ana", "Pedro", "Luis", "Maria"]
        nombres_conjuntos = set(nombres)
        lista_nueva = list(nombres_conjuntos)
        print(lista_nueva)
        print(sorted(lista_nueva))

        print("\n========== ESTUDIANTES APROBADOS ==========")
        estudantes = {"Isaac": 10, "Carlos": 5, "Maria": 10, "Renato": 9, "Itzuki": 10}

        for key, value in estudantes.items():
            if value >= 6:
                print("Estudiante:", key, " | Nota:", value)
    

    def ejercicio5(self):
        print("========== EJE3: BUSQUEDA Y CONVERSION ==========")
        colores = ("rojo", "azul", "verde", "azul")
        print("Tupla original:", colores)

        
        print("¿Cuántas veces está 'azul'?:", colores.count("azul"))
        print("Posición de la primera 'verde':", colores.index("verde"))

        
        lista_temporal = list(colores)
        lista_temporal.append("amarillo")
        nueva_tupla = tuple(lista_temporal)
        
        print("Nueva tupla modificada:", nueva_tupla)