class Eje18:

    def ejercicio1(self):
        print("========== EJE1: TABLA DE MULTIPLICAR ==========")
        print("")
        numero = 7
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

    def ejercicio2(self):
        print("========== EJE2: PARES E IMPARES ==========")
        print("")
        numeros = [10, 7, 4, 3, 8, 15, 22, 9]
        pares = [n for n in numeros if n % 2 == 0]
        impares = [n for n in numeros if n % 2 != 0]
        print(f"Lista original: {numeros}")
        print(f"Pares:   {pares}")
        print(f"Impares: {impares}")

    def ejercicio3(self):
        print("========== EJE3: MAYOR Y MENOR ==========")
        print("")
        numeros = [34, 12, 89, 5, 47, 23]
        print(f"Lista:  {numeros}")
        print(f"Mayor:  {max(numeros)}")
        print(f"Menor:  {min(numeros)}")
        print(f"Suma:   {sum(numeros)}")
        print(f"Promedio: {sum(numeros) / len(numeros)}")

    def ejercicio4(self):
        print("========== EJE4: INVERTIR TEXTO ==========")
        print("")
        texto = "Programacion Orientada a Objetos"
        invertido = texto[::-1]
        print(f"Texto original:  {texto}")
        print(f"Texto invertido: {invertido}")
        print(f"Cantidad de letras: {len(texto)}")

    def ejercicio5(self):
        print("========== EJE5: CONTAR VOCALES ==========")
        print("")
        texto = "inteligencia artificial"
        vocales = "aeiou"
        conteo = {v: 0 for v in vocales}
        for letra in texto.lower():
            if letra in vocales:
                conteo[letra] += 1
        print(f"Texto: {texto}")
        for vocal, cantidad in conteo.items():
            print(f"  '{vocal}' aparece {cantidad} veces")
        total = sum(conteo.values())
        print(f"Total de vocales: {total}")
        