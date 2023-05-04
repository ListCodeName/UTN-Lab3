import random
import datetime
class Task:
    __pid = 0
    __estado = 0
    __nombre = ""
    __fecInicio = None
    __ultMod = None

    def __init__ (self,nombre):
        self.__estado = 1
        self.__nombre = nombre
        self.pid = random.randint(1,1000)
        self.__fecInicio = datetime.datetime.now()
        self.__ultMod = datetime.datetime.now()
    
    def cambiarEstado ():
        pass

    
