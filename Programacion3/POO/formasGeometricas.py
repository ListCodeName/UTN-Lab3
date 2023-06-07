from abc import ABC
class FiguraGeometrica (metaclass=ABCMeta):
    """
    calcular_area(): Calcula y devuelve el área de la forma geométrica.
 calcular_perimetro(): Calcula y devuelve el perímetro de la forma
geométrica.
2. Color: Esta interfaz debe tener el siguiente método abstracto:
 obtener_color(): Devuelve el color de la forma geométrica
    """

    @abstractmethod
    def calcularArea(figura)->float: 
        pass
    @abstractmethod
    def calcularPerimetro(figura)->float:
        pass
    @abstractmethod
    def obtenerColor(figura)->str:
        pass