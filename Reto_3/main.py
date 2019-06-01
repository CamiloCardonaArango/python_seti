""" Módulo principal de ejecución para el reto de la semana 3 """

import clases

def main():
    """ Método principal """
    entrada_a = int(input("Por favor ingrese la entrada A: "))
    entrada_b = int(input("Por favor ingrese la entrada B: "))
    if entrada_a not in(0, 1) or entrada_b not in(0, 1):
        print("Debe ingresar valores entre 0 y 1")
    else:
        compuerta_or = clases.CompuertaOR(entrada_a, entrada_b)
        compuerta_and = clases.CompuertaAND(entrada_a, entrada_b)
        print(compuerta_or.calcular_salida())
        print(compuerta_and.calcular_salida())

main()
