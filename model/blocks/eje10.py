 #  bloques/eje10.py  ── BLOQUE 10 

class Eje10:

    def ejercicio1(self):
        print("========== EJE1: ACCESO A DICCIONARIOS ==========")

        persona = {
            "nombre": "Juan",
            "edad": 25,
            "ciudad": "Babahoyo"
            }
            
        print("\n---- Accediendo con [] ----")
        print("Nombre accediendo con []:", persona["nombre"])
        print("Edad accediendo con []:", persona["edad"])
        print("Ciudad accediendo con []:", persona["ciudad"])

        print("\n---- Accediendo con .get ----")
        print("Nombre accediendo con .get:",persona.get("nombre"))
        print("Edad accediendo con .get:",persona.get("edad"))
        print("Ciudad accediendo con .get:",persona.get("ciudad"))

    def ejercicio2(self):
        print("========== EJE1: ITERACIÓN DE DICCIONARIO CON .ITEM() ==========")
        catalogo = {
            "Nombre": "Carlos", 
            "Edad": 15, 
            "Ciudad": "Guayaquil", 
            "Teléfono":"0985676234" 
            }

        for clave, valor in catalogo.items():
            print(clave, ":", valor)

    def ejercicio3(self):

        print("========== EJE3: ¿REFERENCIA O COPIA? ==========")

        datos = {"a": 1}
        copia = datos
        copia["b"] = 2
        print("\nCASO 1: copia = datos")
        print("  datos =", datos, " <- TAMBIEN cambio!")
        print("  copia =", copia)

        
        datos2 = {"a": 1}
        copia2 = datos2.copy()
        copia2["b"] = 2
        print("\nCASO 2: copia = datos.copy()")
        print("  datos =", datos2, " <- NO cambio :)")
        print("  copia =", copia2)

        print("\nConclusion: usa .copy() para copiar de verdad.")
        
    def ejercicio4(self):
        print("========== EJE4: TIENDA - INVENTARIO ==========")
        inventario = {
            "manzanas": 20,
            "peras": 15,
            "uvas": 30
        }

        print("\n---- Productos en inventario ----")
        for clave, valor in inventario.items():
            print(f"  {clave}: {valor}")

        
        print("\n---- Acceso con [] ----")
        print(f"  Precio de manzanas: {inventario['manzanas']}")

        
        print("\n---- Acceso con .get() ----")
        print(f"  Producto no existente: {inventario.get('telefono')}")
        print(f"  Producto no existente (con default): {inventario.get('telefono', 0)}")

    def ejercicio5(self):
        print("========== EJE5: TIENDA - COPIA Y VENTA ==========")
        inventario = {
            "manzanas": 20,
            "peras": 15,
            "uvas": 30
        }

        print("\n---- Creando respaldo ----")
        respaldo = inventario.copy()
        print(f"  Respaldo creado: {respaldo}")

       
        print("\n---- Vendiendo 5 manzanas ----")
        inventario["manzanas"] -= 5
        print(f"  Venta realizada: -5 manzanas")

        
        print("\n---- Comparacion final ----")
        print(f"  Inventario actual: {inventario}")
        print(f"  Respaldo original: {respaldo}")
        print(f"  ¿El respaldo cambio? -> {inventario == respaldo}")



        

        


                    
                    
                    

                
                
           
                    
     
        

                


                




                
        
