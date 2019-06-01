""" Módulo que contiene las clases utilizadas para el reto de la semana 3"""

class Compuerta:
    """ Clase principal de las compuertas """

    def __init__(self, entrada_a, entrada_b):
        """ Inicializa la clase compuertas """
        self.entrada_a = entrada_a
        self.entrada_b = entrada_b

class CompuertaOR(Compuerta):
    """ Compuerta OR """
    def calcular_salida(self):
        """ Calcula la salida de la compuerta OR """
        salida_or = 1
        if self.entrada_a == 0 and self.entrada_b == 0:
            salida_or = 0
        return "La salida de la compuerta OR es: " + str(salida_or)

class CompuertaAND(Compuerta):
    """ Compuerta AND """
    def calcular_salida(self):
        """ Calcula la salida de la compuerta OR """
        salida_and = 0
        if self.entrada_a == 1 and self.entrada_b == 1:
            salida_and = 1
        return "La salida de la compuerta AND es: " + str(salida_and)
