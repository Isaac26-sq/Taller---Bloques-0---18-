import sys
from view.consola import (
    gotoxy, limpiar, limpiar_ansi, ocultar_cursor, mostrar_cursor, centrar_x,
    CYAN, AMARILLO, GRIS, BLANCO, ROJO, RESET
)
from view.borde import Borde


class EjercicioBox:
   
    ANCHO_MIN = 40
    ALTO_MIN  = 8
    ANCHO_MAX_AUTO = 110
    ALTO_MAX_AUTO  = 28
    PADDING_X = 4

    def __init__(self, titulo, ancho=None, alto=None):
        self.titulo = titulo
        self.padding_x = self.PADDING_X
        ancho_para_titulo = len(titulo) + self.PADDING_X * 2 + 2
        ancho_minimo = max(self.ANCHO_MIN, ancho_para_titulo)
        if ancho is None:
            self.ancho = min(ancho_minimo, self.ANCHO_MAX_AUTO)
        else:
            self.ancho = max(ancho, ancho_minimo)
        self.alto   = alto  if alto  is not None else self.ALTO_MIN
        self.x      = centrar_x(self.ancho)
        self.y      = 2
        self.fila_actual = self.y + 3
        self._lineas_buffer = []
        self._linea_actual  = ""


    def dibujar(self):
       
        limpiar()
        self._dibujar_borde_y_titulo()
        self.fila_actual = self.y + 3
        sys.stdout.flush()

    def _dibujar_borde_y_titulo(self):
        Borde.dibujar(self.x, self.y, self.ancho, self.alto)

        titulo = self.titulo
        limite_titulo = self.ancho - 4
        if len(titulo) > limite_titulo:
            titulo = titulo[:limite_titulo]

        tx = self.x + (self.ancho - len(titulo)) // 2
        gotoxy(tx, self.y + 1)
        print(CYAN + titulo + RESET, end="")

        gotoxy(self.x, self.y + 2)
        print(GRIS + "╠" + "═" * (self.ancho - 2) + "╣" + RESET, end="")
        sys.stdout.flush()

    
    def imprimir(self, texto, color=BLANCO, centrado=False):
       
        if self.fila_actual >= self.y + self.alto - 2:
            return

        if centrado:
            cx = self.x + (self.ancho - len(texto)) // 2
        else:
            cx = self.x + self.padding_x

        gotoxy(cx, self.fila_actual)
        print(color + texto + RESET, end="")
        self.fila_actual += 1
        sys.stdout.flush()

    def salto_linea(self):
        self.fila_actual += 1

    
    def pedir_input(self, etiqueta, validador=None, mensaje_error="Entrada invalida."):
        fila_prompt = self.fila_actual
        fila_error  = self.fila_actual + 1
        px = self.x + self.padding_x

        self.fila_actual += 2
        ancho_limpieza = self.ancho - self.padding_x - 2

        while True:
            gotoxy(px, fila_prompt)
            print(" " * ancho_limpieza, end="")
            gotoxy(px, fila_error)
            print(" " * ancho_limpieza, end="")

            gotoxy(px, fila_prompt)
            print(BLANCO + etiqueta + RESET, end="")
            gotoxy(px + len(etiqueta), fila_prompt)
            mostrar_cursor()
            sys.stdout.flush()

            entrada = input().strip()

            try:
                if validador is None:
                    if entrada == "":
                        raise ValueError("vacío")
                    return entrada
                else:
                    resultado = validador(entrada)
                    if resultado is False:
                        raise ValueError("no válido")
                    return resultado if resultado is not True else entrada
            except Exception:
                ocultar_cursor()
                gotoxy(px, fila_error)
                print(ROJO + "  " + mensaje_error + RESET, end="")
                sys.stdout.flush()

    
    def ejecutar_funcion(self, func, *args, **kwargs):
        stdout_original = sys.stdout
        stdin_original  = sys.stdin

        lineas = [""]

        caja = self

        def redibujar_caja_con(lineas_actuales, esperando_input=False):
            ancho_contenido = max((len(l) for l in lineas_actuales), default=0)
            ancho_contenido = max(ancho_contenido, len(caja.titulo))
            ancho = max(caja.ANCHO_MIN, ancho_contenido + caja.padding_x * 2 + 2)
            ancho = min(ancho, caja.ANCHO_MAX_AUTO)

            alto_contenido = len(lineas_actuales)
            alto = max(caja.ALTO_MIN, alto_contenido + 5)
            alto = min(alto, caja.ALTO_MAX_AUTO)

            caja.ancho = ancho
            caja.alto  = alto
            caja.x     = centrar_x(ancho)

            limpiar()
            caja._dibujar_borde_y_titulo()

            for i, linea in enumerate(lineas_actuales):
                fila = caja.y + 3 + i
                if fila >= caja.y + caja.alto - 1:
                    break
                gotoxy(caja.x + caja.padding_x, fila)
                limite = caja.ancho - caja.padding_x * 2 - 2
                stdout_original.write(linea[:limite])

            if esperando_input and lineas_actuales:
                ultima = lineas_actuales[-1]
                fila = caja.y + 3 + len(lineas_actuales) - 1
                col  = caja.x + caja.padding_x + len(ultima)
                limite_col = caja.x + caja.ancho - 2
                if col > limite_col:
                    col = limite_col
                gotoxy(col, fila)

            stdout_original.flush()

        class StdoutCaptura:
            def write(self, texto):
                if not texto:
                    return 0
                for ch in texto:
                    if ch == "\n":
                        lineas.append("")
                    elif ch == "\r":
                        pass
                    else:
                        lineas[-1] += ch
                return len(texto)

            def flush(self):
                pass

            def isatty(self):
                return False

        import builtins
        input_original = builtins.input

        
        def pedir_varios(campos, contexto=None):
            import msvcrt

            n = len(campos)
            valores = ["" for _ in campos]  
            errores = ["" for _ in campos]   
            resultados_validados = [None for _ in campos]

            
            if contexto is None:
                textos_contexto = []
            elif isinstance(contexto, str):
                textos_contexto = [contexto]
            else:
                textos_contexto = list(contexto)

           
            DECOR = "======"
            lineas_contexto = []
            for t in textos_contexto:
                lineas_contexto.append(f"{DECOR} {t.upper()} {DECOR}")

            
            offset_contexto = len(lineas_contexto) + (1 if lineas_contexto else 0)

            
            etiq_larga = max((len(c["etiqueta"]) for c in campos), default=0)
            ancho_contexto = max((len(l) for l in lineas_contexto), default=0)
            ancho_fijo = max(caja.ANCHO_MIN,
                             etiq_larga + 30 + caja.padding_x * 2 + 2,
                             ancho_contexto + caja.padding_x * 2 + 2,
                             len(caja.titulo) + caja.padding_x * 2 + 2)
            ancho_fijo = min(ancho_fijo, caja.ANCHO_MAX_AUTO)
            alto_fijo = max(caja.ALTO_MIN, n * 2 + 6 + offset_contexto)
            alto_fijo = min(alto_fijo, caja.ALTO_MAX_AUTO)

            caja.ancho = ancho_fijo
            caja.alto = alto_fijo
            caja.x = centrar_x(ancho_fijo)

            limite = caja.ancho - caja.padding_x * 2 - 2

            def fila_de(idx):
              
                return caja.y + 3 + offset_contexto + idx * 2

            def construir_frame():
               
                partes = []
                for i, campo in enumerate(campos):
                    texto = (campo["etiqueta"] + valores[i])[:limite].ljust(limite)
                    fila = fila_de(i)
                    col = caja.x + caja.padding_x
                    partes.append(f"\033[{fila};{col}H{BLANCO}{texto}{RESET}")

                    fila_err = fila + 1
                    if errores[i]:
                        err = ("  " + errores[i])[:limite].ljust(limite)
                        partes.append(f"\033[{fila_err};{col}H{ROJO}{err}{RESET}")
                    else:
                        partes.append(f"\033[{fila_err};{col}H{' ' * limite}")
                return "".join(partes)

            def posicionar_cursor(idx):
                fila = fila_de(idx)
                col = caja.x + caja.padding_x + len(campos[idx]["etiqueta"]) \
                      + len(valores[idx])
               
                return f"\033[{fila};{col}H\033[?25h"

            def render(idx):
               
                from view.borde import Borde
                sys.stdout = stdout_original

                buffer = []
                buffer.append("\033[?25l")         
                buffer.append("\033[2J")            

               
                stdout_original.write("".join(buffer))
                Borde.dibujar(caja.x, caja.y, caja.ancho, caja.alto)

                tx = caja.x + (caja.ancho - len(caja.titulo)) // 2
                stdout_original.write(
                    f"\033[{caja.y + 1};{tx}H{CYAN}{caja.titulo}{RESET}"
                )
                stdout_original.write(
                    f"\033[{caja.y + 2};{caja.x}H{GRIS}"
                    + "╠" + "═" * (caja.ancho - 2) + "╣" + RESET
                )

                
                for i, linea in enumerate(lineas_contexto):
                    fila = caja.y + 3 + i
                    txt = linea[:caja.ancho - 4]
                   
                    col = caja.x + (caja.ancho - len(txt)) // 2
                    stdout_original.write(
                        f"\033[{fila};{col}H{BLANCO}{txt}{RESET}"
                    )

                stdout_original.write(construir_frame())
                stdout_original.write(posicionar_cursor(idx))
                stdout_original.flush()
                sys.stdout = StdoutCaptura()

            def actualizar_linea(idx):
               
                sys.stdout = stdout_original
                texto = (campos[idx]["etiqueta"] + valores[idx])[:limite].ljust(limite)
                fila = fila_de(idx)
                col = caja.x + caja.padding_x
                stdout_original.write("\033[?25l")  
                stdout_original.write(f"\033[{fila};{col}H{BLANCO}{texto}{RESET}")
                stdout_original.write(posicionar_cursor(idx))  
                stdout_original.flush()
                sys.stdout = StdoutCaptura()

            def mostrar_error(idx):
                
                sys.stdout = stdout_original
                fila_err = fila_de(idx) + 1
                col = caja.x + caja.padding_x
                err = ("  " + errores[idx])[:limite].ljust(limite)
                stdout_original.write("\033[?25l")
                stdout_original.write(f"\033[{fila_err};{col}H{ROJO}{err}{RESET}")
                stdout_original.write(posicionar_cursor(idx))
                stdout_original.flush()
                sys.stdout = StdoutCaptura()

            def limpiar_linea_error(idx):
              
                sys.stdout = stdout_original
                fila_err = fila_de(idx) + 1
                col = caja.x + caja.padding_x
                stdout_original.write("\033[?25l")
                stdout_original.write(f"\033[{fila_err};{col}H{' ' * limite}")
                stdout_original.flush()
                sys.stdout = StdoutCaptura()

            def mover_cursor_a(idx):
               
                sys.stdout = stdout_original
                stdout_original.write(posicionar_cursor(idx))
                stdout_original.flush()
                sys.stdout = StdoutCaptura()

            actual = 0
            render(actual)  

            while True:
                tecla = msvcrt.getwch()

                if tecla in ("\r", "\n"):
                    campo = campos[actual]
                    texto = valores[actual].strip()
                    validador = campo.get("validador")
                    hubo_error_antes = bool(errores[actual])
                    try:
                        if validador is None:
                            if texto == "":
                                raise ValueError("vacio")
                            resultados_validados[actual] = texto
                        else:
                            r = validador(texto)
                            if r is False:
                                raise ValueError("invalido")
                            if r is True or r is None:
                                resultados_validados[actual] = texto
                            else:
                                resultados_validados[actual] = r
                        errores[actual] = ""
                        if actual < n - 1:
                          
                            if hubo_error_antes:
                                limpiar_linea_error(actual)
                            actual += 1
                            mover_cursor_a(actual)
                        else:
                            break
                    except Exception:
                        
                        errores[actual] = campo.get("mensaje_error", "Entrada invalida")
                        valores[actual] = ""
                        resultados_validados[actual] = None
                        actualizar_linea(actual)   
                        mostrar_error(actual)     

                elif tecla == "\x08":             
                    if valores[actual]:
                        valores[actual] = valores[actual][:-1]
                        actualizar_linea(actual)
                        if errores[actual]:
                            errores[actual] = ""
                            limpiar_linea_error(actual)
                            mover_cursor_a(actual)

                elif tecla in ("\x00", "\xe0"):   
                    msvcrt.getwch()

                elif tecla == "\t":              
                    actual = (actual + 1) % n
                    mover_cursor_a(actual)

                elif tecla.isprintable():
                    valores[actual] += tecla
                    actualizar_linea(actual)
                  
                    if errores[actual]:
                        errores[actual] = ""
                        limpiar_linea_error(actual)
                        mover_cursor_a(actual)

           
            resultados = []
            for i, campo in enumerate(campos):
                if resultados_validados[i] is not None:
                    resultados.append(resultados_validados[i])
                else:
                    resultados.append(valores[i].strip())

            
            del lineas[len(lineas):]
            for linea_ctx in lineas_contexto:
                lineas.append(linea_ctx)
            if lineas_contexto:
                lineas.append("")   
            for i, campo in enumerate(campos):
                lineas.append(campo["etiqueta"] + valores[i])
                lineas.append("")
            return resultados

        
        from view import entrada as _entrada
        _entrada._registrar(pedir_varios)

        def input_recuadro(prompt="", validador=None, mensaje_error="Entrada invalida"):
            while True:
                linea_prompt_idx = len(lineas) - 1
                for ch in prompt:
                    if ch == "\n":
                        lineas.append("")
                    else:
                        lineas[-1] += ch

                sys.stdout = stdout_original

                redibujar_caja_con(lineas, esperando_input=True)
                mostrar_cursor()
                stdout_original.flush()

                valor = input_original()

                sys.stdout = StdoutCaptura()

                try:
                    if validador is None:
                        if valor.strip() == "":
                            raise ValueError("vacio")
                        lineas[-1] += valor
                        lineas.append("")
                        return valor
                    else:
                        resultado = validador(valor.strip())
                        if resultado is False:
                            raise ValueError("invalido")
                        lineas[-1] += valor
                        lineas.append("")
                        return resultado if resultado is not True else valor.strip()
                except Exception:
                    lineas[-1] += valor
                    lineas.append("  " + ROJO + mensaje_error + RESET)
                    sys.stdout = stdout_original
                    redibujar_caja_con(lineas, esperando_input=False)
                    sys.stdout.flush()

                    import time
                    time.sleep(1.2)  

                    lineas.pop()
                    lineas.pop()
                    lineas.append("")

       
        limpiar()
        try:
            sys.stdout = StdoutCaptura()
            builtins.input = input_recuadro
            resultado = func(*args, **kwargs)
        finally:
            sys.stdout = stdout_original
            builtins.input = input_original
            _entrada._limpiar()

        if lineas and lineas[-1] == "":
            lineas.pop()

        redibujar_caja_con(lineas, esperando_input=False)
        caja.fila_actual = caja.y + 3 + len(lineas)

        return resultado

   
    def esperar_tecla(self):
        import msvcrt
        msg = "Presiona cualquier tecla para volver..."
        fila = self.y + self.alto + 1
        cx = self.x + (self.ancho - len(msg)) // 2
        gotoxy(cx, fila)
        print(GRIS + msg + RESET, end="")
        ocultar_cursor()
        sys.stdout.flush()
        msvcrt.getch()
        mostrar_cursor()
