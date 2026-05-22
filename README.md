# Guía Práctica Experimental 1 — Programación Orientada a Objetos en Python

Aplicación de consola interactiva que reúne **19 bloques temáticos** de Programación
Orientada a Objetos, cada uno con **5 ejercicios** resueltos. La navegación se hace
mediante un menú principal y submenús dibujados directamente en la terminal con
bordes, colores y validación de entradas.

---


## LINK DE IA USADA 
-- https://claude.ai/share/9a92b723-2602-430f-aeb0-4312398ef6f4
## Tabla de contenido

- [Características](#características)
- [Requisitos](#requisitos)
- [Cómo ejecutar](#cómo-ejecutar)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Arquitectura](#arquitectura)
- [Contenido de los bloques](#contenido-de-los-bloques)
- [Cómo agregar un ejercicio o un bloque](#cómo-agregar-un-ejercicio-o-un-bloque)
- [Documentación del uso de IA](#documentación-del-uso-de-ia)

---

## Características

- Menú principal en dos columnas con los **19 bloques** de la guía.
- Submenú por bloque que muestra cada ejercicio con una **descripción breve**.
- Recuadros dibujados con caracteres de borde Unicode, que se **adaptan al ancho**
  del título y del contenido.
- Captura de datos por teclado con **validación campo por campo** y mensajes de
  error claros.
- Arquitectura **Modelo–Vista–Controlador (MVC)** que separa lógica, interfaz y flujo.

---

## Requisitos

- **Python 3.10 o superior**.
- **Sistema operativo Windows**. El proyecto usa los módulos `msvcrt` (lectura de
  teclas) y `ctypes.windll` (modo de consola ANSI), exclusivos de Windows.
- Una ventana de terminal **ancha** (recomendado 150 columnas o más), ya que el
  menú principal y el submenú se dibujan uno al lado del otro.

---

## Cómo ejecutar

Desde la carpeta `proyecto_POO`:

```bash
python main.py
```

Navegación:

1. En el **menú principal**, escribe el número del bloque que quieres abrir.
2. En el **submenú**, escribe el número del ejercicio a ejecutar.
3. Pulsa cualquier tecla para volver al submenú tras ver el resultado.
4. Escribe `0` para volver al menú principal y `S` para salir.

---

## Estructura del proyecto

```
proyecto_POO/
├── main.py                     Punto de entrada de la aplicación
├── README.md                   Este documento
│
├── controller/
│   └── menu_controller.py      Controla el flujo entre menús y ejercicios
│
├── model/
│   └── blocks/
│       ├── eje0.py ... eje18.py  Un archivo por bloque (clase EjeN)
│
├── view/
│   ├── consola.py              Utilidades de consola, colores y posición
│   ├── borde.py                Dibujo de recuadros con bordes
│   ├── menu.py                 Dibujo de menús y captura de la opción
│   ├── ejercicio_box.py        Caja donde se ejecuta cada ejercicio
│   ├── entrada.py              Puente para la captura de varios campos
│   └── etiquetas.py            Nombres de bloques y descripciones
│
└── data/
    ├── archivo.txt             Archivos usados por el bloque 16
    ├── contactos.json
    ├── coordenadas.json
    ├── Agenda_Contactos.json
    └── ventas.Json
```

---

## Arquitectura

El proyecto sigue el patrón **MVC**:

| Capa | Carpeta | Responsabilidad |
|------|---------|-----------------|
| **Modelo** | `model/blocks/` | Contiene la lógica de cada ejercicio. Cada bloque es una clase `EjeN` con métodos `ejercicio1` a `ejercicio5`. |
| **Vista** | `view/` | Todo lo que se dibuja en pantalla: menús, bordes, cajas y captura de datos. |
| **Controlador** | `controller/` | Coordina el flujo: muestra menús, lee la opción del usuario e invoca el ejercicio correspondiente. |

El controlador localiza cada ejercicio **por convención de nombres**: para el bloque
`N` importa el módulo `model.blocks.ejeN`, obtiene la clase `EjeN` y llama al método
`ejercicioM`. Por eso es indispensable respetar esos nombres al añadir contenido.

---

## Contenido de los bloques

| # | Bloque | Ejercicios |
|---|--------|-----------|
| 0 | Introducción a la POO | Identificar clases · Instancias · Clase vs objeto · Métodos y descuentos · Validación de montos |
| 1 | El Constructor `__init__` | Clase Producto · Constructor con validación · Atributo por defecto · `@classmethod` · Clase Libro |
| 2 | Variables y Tipos de Datos | Tipos simples · Imprimir lista · Acceso por índice · Modificar posición · Insertar posición |
| 3 | Operadores y Expresiones | Aritméticos · Lógicos y booleanos · Orden de evaluación · División entera y módulo · `==` vs `is` |
| 4 | Entrada y Salida (input / print) | Lectura con `input()` · Suma de notas · Concatenación · Casting de tipos · Concatenación vs suma |
| 5 | Condicionales (if / elif / else) | Par o impar · Calificación por letra · Login · Positivo/negativo/cero · Validación de acceso |
| 6 | Bucles (for / while) | Contador 1 al 10 · `enumerate` · List comprehension · `range` con paso · Recorrer con `while` |
| 7 | Funciones | Función doble · Suma con `*args` · Factorial recursivo · Invertir string · Filtrar pares |
| 8 | Listas | Agregar y ordenar · Suma/máx/mín · Referencia vs copia · Manipulación · Trucos con tuplas |
| 9 | Tuplas | Inmutabilidad · Unpacking con `*resto` · Recorrer coordenadas · Conjuntos · Búsqueda y conversión |
| 10 | Diccionarios | Acceso · Iteración con `.items()` · Referencia o copia · Tienda inventario · Tienda copia y venta |
| 11 | Conjuntos (set) | Operaciones · Eliminar duplicados · Elementos únicos · Estudiantes y materias · Métodos de conjuntos |
| 12 | Excepciones (try / except) | `ValueError` · `IndexError` · Múltiples errores · `try/except/else/finally` · `raise` |
| 13 | Decoradores | Decorador básico · Verificar positivo · Decorador log · Cronómetro · Mayúsculas |
| 14 | Unpacking (Desempaquetado) | Básico · En funciones con `*` · Combinar dicts con `**` · En bucles · En retorno de funciones |
| 15 | Funciones de Orden Superior | `map()` · `filter()` · `reduce()` · Combinar map y filter · Función de orden superior propia |
| 16 | Archivos y JSON | Lectura/escritura TXT · Guardar y cargar JSON · Recorrer lista JSON · Agenda · Registro de ventas |
| 17 | Mixins | `PromedioMixin` · `ValidacionMixin` · `ExportarMixin` · `LogMixin` · `BusquedaMixin` |
| 18 | Ejercicios Extra | Tabla de multiplicar · Pares e impares · Mayor y menor · Invertir texto · Contar vocales |

---

## Cómo agregar un ejercicio o un bloque

**Agregar un ejercicio a un bloque existente**

1. En `model/blocks/ejeN.py`, añade un método `ejercicioM` dentro de la clase `EjeN`.
2. En `controller/menu_controller.py`, ajusta la constante `NUM_EJERCICIOS`.
3. En `view/etiquetas.py`, añade la descripción del ejercicio en
   `DESCRIPCIONES_EJERCICIOS`.

**Agregar un bloque nuevo**

1. Crea `model/blocks/ejeN.py` con una clase `EjeN` y sus métodos `ejercicio1`…`ejercicio5`.
2. En `controller/menu_controller.py`, aumenta `NUM_BLOQUES`.
3. En `view/etiquetas.py`, añade el bloque tanto en `NOMBRES_BLOQUES` como en
   `DESCRIPCIONES_EJERCICIOS`.

> Regla clave: el archivo se llama `ejeN.py`, la clase `EjeN` y los métodos
> `ejercicioM` correlativos desde 1. Si alguno no coincide, el controlador no
> encontrará el ejercicio.

---

## Documentación del uso de IA

Según las indicaciones de la guía, esta sección documenta el uso de herramientas de
Inteligencia Artificial. Por cada ejercicio se registra: la IA utilizada, el prompt
para **entender** el ejercicio y el prompt para **generar un proceso similar** de
práctica.

> Completa la tabla siguiente con los prompts reales que utilizaste. Se incluye un
> ejemplo en la primera fila como referencia de formato.

| Bloque / Ejercicio | IA utilizada | Prompt para entender el ejercicio | Prompt para generar un proceso similar |
|--------------------|--------------|-----------------------------------|----------------------------------------|
| Bloque 17 — Ej. 1 (PromedioMixin) | *(ejemplo)* Claude | "Explícame qué es un Mixin en Python y cómo crear un `PromedioMixin` que calcule el promedio de una lista de notas." | "Genérame un ejercicio parecido con un Mixin distinto para practicar por mi cuenta, sin darme la solución." |
| Bloque 0 — Ej. … |  |  |  |
| Bloque 1 — Ej. … |  |  |  |
| Bloque 2 — Ej. … |  |  |  |
| … |  |  |  |

### Metodología de aprendizaje

El objetivo del uso de IA en este proyecto **no es copiar respuestas**, sino:

- Desarrollar el pensamiento lógico.
- Aprender a formular buenas preguntas.
- Usar la IA como herramienta de apoyo al aprendizaje.
- Comprender realmente cada proceso.

El ciclo seguido en cada ejercicio fue: **explicación → proceso similar → resolución
propia**, repitiéndolo hasta comprender por completo el proceso original.

---

## Autor

Proyecto desarrollado como parte de la **Guía Práctica Experimental 1** de la
asignatura de Programación Orientada a Objetos.

*Completa aquí tu nombre, carrera y fecha de entrega.*
