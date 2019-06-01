""" Módulo que contiene las funciones utilizadas para el reto de la semana 2"""

import xlrd

def crear_archivo():
    """crea el archivo con el resultado de las operaciones"""
    print("prueba")

def calcular_excel(p_nombre_archivo):
    """lee el archivo de excel y escribe los resultados en archivo txtx"""
    try:
        with open('Reto_2/resultados.txt', 'w') as archivo_resultado:
            with xlrd.open_workbook(p_nombre_archivo) as libro:
                for numero_hoja in range(libro.nsheets):
                    hoja = libro.sheet_by_index(numero_hoja)
                    total_filas = hoja.nrows
                    nombre_hoja = hoja.name
                    for fila in range(1, total_filas):
                        numero_1 = 0
                        numero_2 = 0
                        valores = hoja.row_values(fila)
                        try:
                            numero_1 = int(valores[0])
                            numero_2 = int(valores[1])
                            if nombre_hoja == "SUMA":
                                resultado = numero_1 + numero_2
                            elif nombre_hoja == "RESTA":
                                resultado = numero_1 - numero_2
                            elif nombre_hoja == "MULTIPLICACIÓN":
                                resultado = numero_1 * numero_2
                            elif nombre_hoja == "DIVISIÓN":
                                resultado = numero_1 / numero_2
                        except ValueError:
                            resultado = "Error"
                        except ZeroDivisionError:
                            resultado = "Error"
                        archivo_resultado.write(str(resultado) + '\n')
    except BaseException:
        print("Se presntó un error")
        