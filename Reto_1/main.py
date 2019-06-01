""" Módulo principal del reto de la semana 1"""
import funciones

def main():
    """ Función principal """
    palabra = input("Por favor digite una palabra: ")
    if funciones.valida_palindroma(palabra):
        print("La palabra " + palabra + " SI es palíndroma")
    else:
        print("La palabra " + palabra + " NO es palíndroma")
main()
