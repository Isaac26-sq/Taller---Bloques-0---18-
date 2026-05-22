# BLOQUE 1: CONSTRUCTOR __init__

class Eje1:
   

    def ejercicio1(self):
        class Producto:
            def __init__(self, codigo, nombre, precio):
                self.codigo = codigo
                self.nombre = nombre
                self.precio = precio

            def montrar_info(self):
                print(f"Codigo: {self.codigo} | Nombre: {self.nombre} | Precio: {self.precio}")

        product1 = Producto(1, "Aceite", 1)
        product2 = Producto(2, "Mi Vaquita", 3)
        print(" Crea la clase Producto con código, nombre y precio.")
        print("Id:", product1.codigo, " Producto:",product1.nombre," Precio:",product1.precio)
        print("Id:",product2.codigo, " Producto:",product2.nombre," Precio:",product2.precio)

    def ejercicio2(self):
        class Telefono:
            def __init__(self, marca, modelo, precio):
                if precio < 0:
                    raise ValueError(f"Precio negativo: {precio}")
                self.marca = marca
                self.modelo = modelo
                self.precio = precio

            def marca_info(self):
                print(f"Marca: {self.marca}| Modelo: {self.modelo} | Precio: {self.precio}")

        tele1 = Telefono("Xiaomi", "Note 14 Pro", -900)
        tele1.marca_info()

    def ejercicio3(self):
        class Estudiante:
            def __init__(self, nombre, notas=None):
                self.nombre = nombre
                self.notas = notas

                if notas is None:
                    self.notas = []

            def calcular_promedio(self):
                if self.notas:
                    promedio = round(sum(self.notas) / len(self.notas), 2)
                    print(f"Nombre: {self.nombre} | Notas: {self.notas} | Promedio: {promedio}")
                else:
                    print(f"{self.nombre}: No hay notas registradas")

        estu1 = Estudiante("Isaac Silva", notas=[10, 10, 9])
        estu2 = Estudiante("Maria Alvarez")
        print("")
        print("- Crea Estudiante con nombre y notas")
        print("\n--- Nomina ---")
        estu1.calcular_promedio()
        estu2.calcular_promedio()
        print("")

    def ejercicio4(self):
        class Estudiante:
            def __init__(self, nombre, carrera, semestre, edad):
                self.nombre = nombre
                self.carrera = carrera
                self.semestre = semestre
                self.edad = edad

            @classmethod
            def from_dicc(cls, datos):
                return cls(datos["Nombre"], datos["Carrera"], datos["Semestre"], datos["Edad"])

        datos = {"Nombre": "Isaac Silva", "Carrera": "Software", "Semestre": "Cuarto", "Edad": 20}
        estu1 = Estudiante.from_dicc(datos)
        print("Agrega un @classmethod desde_diccionario que cree un Estudiante")
        print("\nNombre:",estu1.nombre,"| Carrera:",estu1.carrera,"| Semestre:",estu1.semestre,"| Edad:",estu1.edad)

    def ejercicio5(self):
        class Libro:
            def __init__(self, titulo, autor, año):
                self.titulo = titulo
                self.autor = autor
                self.año = año

            @classmethod
            def from_dicc(cls, dato):
                return cls(dato["titulo"], dato["autor"], dato["anio"])

            @classmethod
            def from_text(cls, dato):
                partes = dato.split(",")
                return cls(partes[0], partes[1], partes[2])

        dato = {"titulo": "El Principito", "autor": "Antoine de Saint-Exupery", "anio": 1943}
        
        print("- Crea una clase Libro con los atributos titulo, autor y año.")

        libro1 = Libro.from_text("Cien anios de soledad, Garcia Marquez , 1067")
        print("\nTitulo:",libro1.titulo,"| Autor:",libro1.autor,"| Año:",libro1.año)

        libro = Libro.from_dicc(dato)
        print("\nTitulo:",libro.titulo,"| Autor:",libro.autor,"| Año:",libro.año)
