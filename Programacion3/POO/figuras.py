from formasGeometricas import FiguraGeometrica

class Color:
    def __init__(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = codigo

    def getNombre (self):
        return self.__nombre

    def getCodigo (self):
        return self.__codigo


class Circulo (FiguraGeometrica):
    def __init__(self, radio, color):
        self.__radio = radio
        self.__color = color

    def __str__()->str:
        return f"Circulo de color  de radio: {self.__radio} "

    def calcularArea(self):
        pass

class Cuadrado (FiguraGeometrica):
    def __init__(self, lado, color):
        self.__lado = lado
        self.__color = color