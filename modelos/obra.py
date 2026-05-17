# modelos/obra.py
from datetime import datetime

class Obra:
    """Clase Obra que utiliza composición de trabajadores y materiales.

    Ahora incluye atributos opcionales `codigo`, `presupuesto` y `estado`.
    """

    def __init__(self, nombre, ubicacion, codigo=None, presupuesto=0, fecha_inicio=None, fecha_fin=None, porcentaje_avance=0, estado='En ejecución'):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        # Atributo opcional: código identificador de la obra
        self.__codigo = codigo
        # Presupuesto total estimado de la obra (numérico)
        self.__presupuesto = presupuesto
        # Fecha de inicio en formato DD/MM/AAAA (string)
        self.__fecha_inicio = fecha_inicio
        # Fecha de fin en formato DD/MM/AAAA (string)
        self.__fecha_fin = fecha_fin
        # Porcentaje de avance (entero 0-100)
        self.__porcentaje_avance = int(porcentaje_avance) if porcentaje_avance is not None else 0
        # Estado de la obra: En ejecución, Liquidada, Suspendida, Por iniciar
        self.__estado = estado
        self.__trabajadores = []
        self.__materiales = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_ubicacion(self):
        return self.__ubicacion

    def set_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    def get_trabajadores(self):
        return self.__trabajadores

    def get_materiales(self):
        return self.__materiales

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_presupuesto(self):
        return self.__presupuesto

    def get_presupuesto_formateado(self):
        presupuesto = self.__presupuesto or 0
        return f"${presupuesto:,.0f}".replace(",", ".")

    def set_presupuesto(self, presupuesto):
        self.__presupuesto = presupuesto

    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def set_fecha_inicio(self, fecha):
        self.__fecha_inicio = fecha

    def get_fecha_fin(self):
        return self.__fecha_fin

    def set_fecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin

    def get_fecha_inicio_formateada(self):
        if not self.__fecha_inicio:
            return ''
        try:
            fecha = datetime.strptime(self.__fecha_inicio, '%d/%m/%Y')
            meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
            return f"{fecha.day:02d}-{meses[fecha.month - 1]}-{fecha.year}"
        except ValueError:
            return self.__fecha_inicio

    def get_fecha_fin_formateada(self):
        if not self.__fecha_fin:
            return ''
        try:
            fecha = datetime.strptime(self.__fecha_fin, '%d/%m/%Y')
            meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
            return f"{fecha.day:02d}-{meses[fecha.month - 1]}-{fecha.year}"
        except ValueError:
            return self.__fecha_fin

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def esta_en_ejecucion(self):
        return self.__estado == 'En ejecución'

    def esta_vencida(self):
        if not self.__fecha_fin:
            return False
        try:
            return datetime.strptime(self.__fecha_fin, '%d/%m/%Y').date() < datetime.now().date()
        except ValueError:
            return False

    def get_porcentaje_avance(self):
        return self.__porcentaje_avance

    def set_porcentaje_avance(self, porcentaje):
        try:
            valor = int(porcentaje)
        except (TypeError, ValueError):
            valor = 0
        # clamp between 0 y 100
        if valor < 0:
            valor = 0
        if valor > 100:
            valor = 100
        self.__porcentaje_avance = valor

    def agregar_trabajador(self, trabajador):
        # Composición: la obra contiene objetos Trabajador.
        self.__trabajadores.append(trabajador)

    def agregar_material(self, material):
        # Composición: la obra contiene objetos Material.
        self.__materiales.append(material)

    def calcular_costo_total(self):
        # Método de instancia que recorre sus materiales para sumar costos.
        total_materiales = sum(material.calcular_costo() for material in self.__materiales)
        total_salarios = sum(trabajador.get_salario() for trabajador in self.__trabajadores)
        return total_materiales + total_salarios

    def calcular_gasto_total(self):
        # Retorna la suma de los costos de todos los materiales de la obra.
        return sum(material.calcular_costo() for material in self.__materiales)
