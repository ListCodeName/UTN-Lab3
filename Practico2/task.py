import random
import datetime
class Task:
    __pid = 0
    __estado = 0
    __nombre = ""
    __fecInicio = None
    __ultMod = None

    def __init__ (self,nombre, pid):
        self.__estado = 1
        self.__nombre = nombre
        self.__pid = pid
        self.__fecInicio = datetime.datetime.now()
        self.__ultMod = datetime.datetime.now()
    
    def cambiarEstado (self, estado):
        self.__estado = estado
        self.__ultMod = datetime.datetime.now()

    def __str__(self):
        return f"{self.__pid} - {self.__nombre} - Status: {self.__calcularEstado()} - Ultima modificación: {self.__calcularModificacion()}"

    def __calcularEstado(self)-> str:
        if(self.__pid == -1):
            return "Dormido"
        if(self.__pid == 0):
            return "Listo"
        if(self.__pid == 1):
            return "En ejecución"
    
    def __calcularModificacion(self)->str:
        minutos = self.__ultMod - self.__fecInicio
        if(minutos < 60):
            return f"{minutos} mins"
        else:
            return f"{int(minutos/60)} hrs"
    
    def getPid(self)->int:
        return self.__pid