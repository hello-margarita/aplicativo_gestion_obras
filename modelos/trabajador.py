# modelos/trabajador.py

class Trabajador:
    """Clase base Trabajador que representa a una persona en la obra."""

    def __init__(self, nombre, cedula, salario, fecha_ingreso="", estado_laboral="Activo", cargo=None):
        # Atributos privados: encapsulamiento para proteger los datos.
        self.__nombre = nombre
        self.__cedula = cedula
        self.__salario = salario
        self.__fecha_ingreso = fecha_ingreso
        self.__estado_laboral = estado_laboral if estado_laboral in ("Activo", "Retirado") else "Activo"
        self.__cargo = cargo or self.__class__.__name__

    # Getters y setters: permiten acceder y modificar atributos privados.
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_cedula(self):
        return self.__cedula

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def get_salario_formateado(self):
        try:
            return f"${self.__salario:,.0f}".replace(",", ".")
        except (TypeError, ValueError):
            return str(self.__salario)

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def set_fecha_ingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso

    def get_estado_laboral(self):
        return self.__estado_laboral

    def set_estado_laboral(self, estado_laboral):
        if estado_laboral in ("Activo", "Retirado"):
            self.__estado_laboral = estado_laboral

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_fecha_ingreso_formateada(self):
        fecha = self.__fecha_ingreso
        meses = {
            "01": "Ene",
            "02": "Feb",
            "03": "Mar",
            "04": "Abr",
            "05": "May",
            "06": "Jun",
            "07": "Jul",
            "08": "Ago",
            "09": "Sep",
            "10": "Oct",
            "11": "Nov",
            "12": "Dic",
        }
        partes = fecha.split("/") if isinstance(fecha, str) else []
        if len(partes) == 3:
            dia, mes, ano = partes
            return f"{dia}-{meses.get(mes, mes)}-{ano}"
        return fecha

    def describir_rol(self):
        # Método de instancia que puede ser sobrescrito por las subclases.
        return f"Trabajador {self.__nombre} con cédula {self.__cedula}."


class Obrero(Trabajador):
    """Subclase Obrero que hereda de Trabajador."""

    def describir_rol(self):
        # Polimorfismo: cada subclase implementa su propia versión del método.
        return f"Obrero {self.get_nombre()} (cédula {self.get_cedula()}) trabaja con herramientas y mano de obra."


class Ingeniero(Trabajador):
    """Subclase Ingeniero que hereda de Trabajador."""

    def describir_rol(self):
        return f"Ingeniero {self.get_nombre()} (cédula {self.get_cedula()}) supervisa la ejecución técnica."


class Arquitecto(Trabajador):
    """Subclase Arquitecto que hereda de Trabajador."""

    def describir_rol(self):
        return f"Arquitecto {self.get_nombre()} (cédula {self.get_cedula()}) diseña y planifica la obra."
