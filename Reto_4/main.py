""" Módulo principal de ejecución para el reto de la semana 4 """

import funciones

def main():
    """ Método principal """
    try:
        print("*** CRUD EMPLEADOS ****")
        print("Opciones:")
        print("(1) Crear")
        print("(2) Consultar")
        print("(3) Actualizar")
        print("(4) Borrar")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            funciones.ejecutar_opcion_1_3(1)
        elif opcion == 2:
            funciones.ejecutar_opcion_2()
        elif opcion == 3:
            funciones.ejecutar_opcion_1_3(3)
        elif opcion == 4:
            funciones.ejecutar_opcion_4()
        else:
            print("Opción inválida")
    except ValueError:
        print("Debe ingresar un número.")

main()
