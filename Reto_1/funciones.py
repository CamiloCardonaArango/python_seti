"""Módulo que contiene las funciones del reto de la semana 1"""

def valida_palindroma(p_palabra):
    """Valida si una palabra es palínfroma."""
    return bool(p_palabra.upper() == p_palabra[::-1].upper())
