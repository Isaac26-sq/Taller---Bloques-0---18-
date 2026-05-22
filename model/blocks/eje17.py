
#  bloques/eje17.py  ── BLOQUE 17 

import json

class Eje17:

   

    class PromedioMixin:
        def calcular_promedio(self, notas):
            return sum(notas) / len(notas)

    class Estudiante(PromedioMixin):
        def __init__(self, nombre, notas):
            self.nombre = nombre
            self.notas  = notas

        def mostrar_promedio(self):
            promedio = self.calcular_promedio(self.notas)
            print(f"  Estudiante: {self.nombre}")
            print(f"  Notas:      {self.notas}")
            print(f"  Promedio:   {promedio}")

    def ejercicio1(self):
        print("========== EJE1: PromedioMixin ==========")

        print("\n---- Creando estudiante ----")
        e1 = self.Estudiante("Daniel", [8, 9, 10])
        e1.mostrar_promedio()

        print()
        e2 = self.Estudiante("Eduardo", [6, 7, 8, 9])
        e2.mostrar_promedio()

   

    class ValidacionMixin:
        def validar_email(self, correo):
            return "@" in correo and ".com" in correo

        def validar_edad(self, edad):
            return edad >= 18

    class Usuario(ValidacionMixin):
        def __init__(self, nombre, correo, edad):
            self.nombre = nombre
            self.correo = correo
            self.edad   = edad

        def registrar(self):
            print(f"  Usuario: {self.nombre}")

            if self.validar_email(self.correo):
                print(f"  Email:   {self.correo} -> valido")
            else:
                print(f"  Email:   {self.correo} -> invalido (debe tener @ y .com)")

            if self.validar_edad(self.edad):
                print(f"  Edad:    {self.edad} -> valida")
            else:
                print(f"  Edad:    {self.edad} -> invalida (debe ser mayor o igual a 18)")

    def ejercicio2(self):
        print("========== EJE2: ValidacionMixin ==========")

        print("\n---- Usuario con datos validos ----")
        u1 = self.Usuario("Daniel", "daniel@gmail.com", 20)
        u1.registrar()

        print("\n---- Usuario con datos invalidos ----")
        u2 = self.Usuario("Invitado", "sincorreo", 15)
        u2.registrar()

  

    class ExportarMixin:
        def exportar_json(self, datos):
            return json.dumps(datos, indent=2, ensure_ascii=False)

        def exportar_csv(self, datos):
            if not datos:
                return ""
            encabezado = ",".join(datos[0].keys())
            filas = [",".join(str(v) for v in fila.values()) for fila in datos]
            return "\n".join([encabezado] + filas)

    class Reporte(ExportarMixin):
        def __init__(self, titulo, datos):
            self.titulo = titulo
            self.datos  = datos

        def mostrar(self):
            print(f"  Reporte: {self.titulo}")
            print(f"  Registros: {len(self.datos)}")

    def ejercicio3(self):
        print("========== EJE3: ExportarMixin ==========")

        ventas = [
            {"producto": "Laptop",  "precio": 800, "cantidad": 3},
            {"producto": "Mouse",   "precio": 25,  "cantidad": 10},
            {"producto": "Teclado", "precio": 45,  "cantidad": 7},
        ]

        reporte = self.Reporte("Ventas del mes", ventas)
        reporte.mostrar()

        print("\n---- Exportando a JSON ----")
        print(reporte.exportar_json(ventas))

        print("\n---- Exportando a CSV ----")
        print(reporte.exportar_csv(ventas))

  

    class LogMixin:
        def log_info(self, mensaje):
            print(f"  [INFO]  {mensaje}")

        def log_error(self, mensaje):
            print(f"  [ERROR] {mensaje}")

        def log_exito(self, mensaje):
            print(f"  [OK]    {mensaje}")

    class SistemaInventario(LogMixin):
        def __init__(self):
            self.productos = {}

        def agregar(self, nombre, cantidad):
            self.log_info(f"Agregando '{nombre}' con cantidad {cantidad}...")
            if cantidad < 0:
                self.log_error(f"Cantidad invalida para '{nombre}'")
                return
            self.productos[nombre] = cantidad
            self.log_exito(f"'{nombre}' agregado correctamente")

        def mostrar(self):
            print(f"  Inventario: {self.productos}")

    def ejercicio4(self):
        print("========== EJE4: LogMixin ==========")

        print("\n---- Operaciones en inventario ----")
        inv = self.SistemaInventario()
        inv.agregar("Laptop", 5)
        inv.agregar("Mouse", 12)
        inv.agregar("Cable", -3)

        print()
        inv.mostrar()

  

    class BusquedaMixin:
        def buscar_por_nombre(self, lista, nombre):
            return [item for item in lista if item["nombre"].lower() == nombre.lower()]

        def buscar_por_campo(self, lista, campo, valor):
            return [item for item in lista if item.get(campo) == valor]

    class CatalogoProductos(BusquedaMixin):
        def __init__(self, productos):
            self.productos = productos

        def mostrar(self, resultados):
            if resultados:
                for r in resultados:
                    print(f"  -> {r}")
            else:
                print("  Sin resultados.")

    def ejercicio5(self):
        print("========== EJE5: BusquedaMixin ==========")

        productos = [
            {"nombre": "Laptop",  "categoria": "Electronica", "precio": 800},
            {"nombre": "Mouse",   "categoria": "Electronica", "precio": 25},
            {"nombre": "Silla",   "categoria": "Muebles",     "precio": 150},
            {"nombre": "Lampara", "categoria": "Muebles",     "precio": 40},
        ]

        catalogo = self.CatalogoProductos(productos)

        print("\n---- Buscar por nombre: 'Mouse' ----")
        catalogo.mostrar(catalogo.buscar_por_nombre(productos, "Mouse"))

        print("\n---- Buscar por categoria: 'Muebles' ----")
        catalogo.mostrar(catalogo.buscar_por_campo(productos, "categoria", "Muebles"))

        print("\n---- Buscar nombre que no existe: 'Tablet' ----")
        catalogo.mostrar(catalogo.buscar_por_nombre(productos, "Tablet"))
