#  bloques/eje16.py  ── BLOQUE 16 

import json

class Eje16:
    

    def ejercicio1(self):
        print("========== EJE1: LECTURA Y ESCRITURA TXT ==========")
        with open("archivo.txt", "w") as f:
            f.write("Python\n")
        print("Archivo escrito correctamente...")
        with open("archivo.txt", "r") as f:
            contenido = f.read()
            print("Contenido:", contenido)
        print("Finalizando...")

    def ejercicio2(self):
        print("========== EJE2: GUARDAR Y CARGAR JSON ==========")
        coordenadas = {"x":10, "y":20}
        with open("coordenadas.json", "w") as f:
            json.dump(coordenadas, f, indent=2)
        print("Archivo JSON guardado correctamente...")
        with open("coordenadas.json", "r") as f:
            cargado = json.load(f)
            print("Coordenada X:", cargado['x'])
            print("Coordenada Y:", cargado['y'])
        print("Finalizando...")

    def ejercicio3(self):
        print("========== EJE3: RECORRIDO DE LISTA JSON ==========")
        Estudiante = [{"Nombre":"Carla"},{"Nombre":"Jesus"}]
        print("Estudiantes registrados:")
        for i in Estudiante:
            print(" -", i['Nombre'])
        print("Finalizando...")
    
    def ejercicio4(self):
        print("========== EJE4: AGENDA DE CONTACTOS ==========")

        contactos = [
            {"nombre": "Isaac Silva",  "telefono": "0991234567", "email": "isaac@gmail.com"},
            {"nombre": "Maria Alvarez","telefono": "0987654321", "email": "maria@gmail.com"},
            {"nombre": "Carlos Perez", "telefono": "0976543210", "email": "carlos@gmail.com"}
        ]

        with open("contactos.json", "w") as f:
            json.dump(contactos, f, indent=2)
        print("Archivo JSON guardado correctamente...")

        print("\n--- Contactos registrados ---")
        with open("contactos.json", "r") as f:
            cargado = json.load(f)
            for contacto in cargado:
                print(f" - {contacto['nombre']} | {contacto['telefono']}")

        print("\n--- Buscar contacto ---")
        buscar = input("Ingrese un nombre: ")

        encontrado = False
        for contacto in cargado:
            if buscar == contacto['nombre']:
                print("\n--- Datos del contacto ---")
                print(f" Nombre   : {contacto['nombre']}")
                print(f" Teléfono : {contacto['telefono']}")
                print(f" Email    : {contacto['email']}")
                encontrado = True
                break

        if not encontrado:
            print("Contacto no encontrado")

    def ejercicio5(self):
        print("========== EJE5: REGISTRO DE VENTAS ==========")
        ventas = [
            {"producto": "Laptop",   "cantidad": 3,  "precio": 800},
            {"producto": "Teclado",  "cantidad": 10, "precio": 50},
            {"producto": "Monitor",  "cantidad": 5,  "precio": 300},
            {"producto": "Mouse",    "cantidad": 15, "precio": 25}
        ]

        with open("ventas.Json", "w") as f:
            json.dump(ventas, f, indent=2)
        print("Archivo JSON guardado correctamente...")

        print("\n--- Total por venta ---")
        with open("ventas.Json", "r") as f:
            cargado = json.load(f)
            lista = []

            for producto in cargado:
                total = producto['cantidad'] * producto['precio']
                lista.append(total)
                print(f" - {producto['producto']:<10} | Total: ${total}")

            mayor = max(lista)

            print("\n--- Venta con mayor total ---")
            for i in cargado:
                total = i['cantidad'] * i['precio']
                if total == mayor:
                    print(f" Producto : {i['producto']}")
                    print(f" Cantidad : {i['cantidad']}")
                    print(f" Precio   : ${i['precio']}")
                    print(f" Total    : ${mayor}")



                


            
            

        



                
          

        






        


        

                    
        
           
