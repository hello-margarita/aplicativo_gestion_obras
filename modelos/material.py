# modelos/material.py

class Material:
    """Clase Material que representa un recurso utilizado en la obra."""

    def __init__(self, nombre, unidad, precio_unitario, cantidad):
        # Encapsulamiento con atributos privados.
        self.__nombre = nombre
        self.__unidad = unidad
        self.__precio_unitario = precio_unitario
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_unidad(self):
        return self.__unidad

    def set_unidad(self, unidad):
        self.__unidad = unidad

    def get_precio_unitario(self):
        return self.__precio_unitario

    def set_precio_unitario(self, precio_unitario):
        self.__precio_unitario = precio_unitario

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def calcular_costo(self):
        # Método de instancia que calcula el costo total del material.
        return self.__precio_unitario * self.__cantidad
