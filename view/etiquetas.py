
NOMBRES_BLOQUES = {
    0:  "Introduccion a la POO",
    1:  "El Constructor __init__",
    2:  "Variables y Tipos de Datos",
    3:  "Operadores y Expresiones",
    4:  "Entrada y Salida (input / print)",
    5:  "Condicionales (if / elif / else)",
    6:  "Bucles (for / while)",
    7:  "Funciones",
    8:  "Listas",
    9:  "Tuplas",
    10: "Diccionarios",
    11: "Conjuntos (set)",
    12: "Excepciones (try / except)",
    13: "Decoradores",
    14: "Unpacking (Desempaquetado)",
    15: "Funciones de Orden Superior",
    16: "Archivos y JSON",
    17: "Mixins",
    18: "Ejercicios Extra",
    19: "Bloque 19",
}


DESCRIPCIONES_EJERCICIOS = {
    0: {
        1: "Identificar clases de un sistema",
        2: "Instancias de una clase",
        3: "Diferencia entre clase y objeto",
        4: "Metodos y descuentos",
        5: "Validacion de montos",
    },
    1: {
        1: "Clase Producto con atributos",
        2: "Constructor con validacion",
        3: "Atributo por defecto (notas)",
        4: "@classmethod desde diccionario",
        5: "Clase Libro",
    },
    2: {
        1: "Variables de tipo simple",
        2: "Imprimir una lista",
        3: "Acceso por indice",
        4: "Modificar una posicion",
        5: "Insertar en una posicion",
    },
    3: {
        1: "Operaciones aritmeticas",
        2: "Operadores logicos y booleanos",
        3: "Orden de evaluacion",
        4: "Division entera y modulo",
        5: "Referencia en memoria (== vs is)",
    },
    4: {
        1: "Lectura de datos con input()",
        2: "Suma total de notas",
        3: "Concatenacion de strings",
        4: "Casting de tipos",
        5: "Concatenacion vs suma",
    },
    5: {
        1: "Numero par o impar",
        2: "Calificacion por letra",
        3: "Sistema de login",
        4: "Numero positivo, negativo o cero",
        5: "Validacion de acceso",
    },
    6: {
        1: "Contador del 1 al 10",
        2: "Recorrido de lista con enumerate",
        3: "List comprehension",
        4: "Bucle con range y paso",
        5: "Recorrer nombres con while",
    },
    7: {
        1: "Funcion doble",
        2: "Suma con *args",
        3: "Factorial recursivo",
        4: "Invertir string con for",
        5: "Filtrar numeros pares",
    },
    8: {
        1: "Agregar y ordenar elementos",
        2: "Suma, maximo y minimo",
        3: "Referencia vs copia",
        4: "Manipulacion de listas",
        5: "Trucos con tuplas",
    },
    9: {
        1: "Inmutabilidad de tuplas",
        2: "Unpacking con *resto",
        3: "Recorrido de coordenadas",
        4: "Operaciones con conjuntos",
        5: "Busqueda y conversion",
    },
    10: {
        1: "Acceso a diccionarios",
        2: "Iteracion con .items()",
        3: "Referencia o copia",
        4: "Tienda - inventario",
        5: "Tienda - copia y venta",
    },
    11: {
        1: "Operaciones con conjuntos",
        2: "Eliminar duplicados con set",
        3: "Elementos unicos no compartidos",
        4: "Estudiantes y materias",
        5: "Metodos de conjuntos",
    },
    12: {
        1: "Capturar ValueError",
        2: "Capturar IndexError",
        3: "Manejo de multiples errores",
        4: "try / except / else / finally",
        5: "Lanzar errores con raise",
    },
    13: {
        1: "Decorador basico",
        2: "Decorador verificar positivo",
        3: "Decorador de log",
        4: "Decorador cronometro",
        5: "Decorador mayusculas",
    },
    14: {
        1: "Desempaquetado basico",
        2: "Unpacking en funciones con *",
        3: "Combinar diccionarios con **",
        4: "Unpacking en bucles",
        5: "Unpacking en retorno de funciones",
    },
    15: {
        1: "map() - incrementar elementos",
        2: "filter() - filtrar elementos",
        3: "reduce() - multiplicar todos",
        4: "Combinar map() y filter()",
        5: "Funcion de orden superior propia",
    },
    16: {
        1: "Lectura y escritura de TXT",
        2: "Guardar y cargar JSON",
        3: "Recorrido de lista JSON",
        4: "Agenda de contactos",
        5: "Registro de ventas",
    },
    17: {
        1: "PromedioMixin",
        2: "ValidacionMixin",
        3: "ExportarMixin",
        4: "LogMixin",
        5: "BusquedaMixin",
    },
    18: {
        1: "Tabla de multiplicar",
        2: "Pares e impares",
        3: "Mayor y menor de una lista",
        4: "Invertir texto",
        5: "Contar vocales",
    },
    19: {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
    },
}


def nombre_bloque(num_bloque):
    return NOMBRES_BLOQUES.get(num_bloque, f"Bloque {num_bloque}")


def descripcion_ejercicio(num_bloque, num_ejercicio):
    return DESCRIPCIONES_EJERCICIOS.get(num_bloque, {}).get(
        num_ejercicio, f"Ejercicio {num_ejercicio}"
    )
