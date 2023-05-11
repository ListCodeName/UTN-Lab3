from task import Task
import random, datetime
from tinydb import TinyDB, Query
import json

class Admin:
    def __init__(self):
        self.listaDeTareas = []
        self.__cargarLista()
        

    def addTask(self, nombre):
        nuevoPid = 1
        flag = True
        #print(self.listaDeTareas)
        while(flag):
            flag = False
            if(len(self.listaDeTareas)!= 0):
                for x in self.listaDeTareas:
                    if( nuevoPid == x.getPid()):
                        nuevoPid = random.randint(1,1000)
                        flag = True
                        break
        nuevaTarea = Task(nuevoPid,nombre,None,None,None)
        self.listaDeTareas.append(nuevaTarea)
        self.__insertarTarea(nuevaTarea)
            
    def getTask(self, pid)->Task:
        for x in self.listaDeTareas:
            if(pid == Task(x).getPid()):
                return x

    def statusUpdate(self, pid, estado):
        aux = None
        for x in self.listaDeTareas:
            if( pid == x.getPid()):
                aux = x
                break
        if(aux == None):
            raise Exception(f"El id {pid} no se encuentra en la lista de tareas.")
        else:
            aux.cambiarEstado(estado)
            self.__updateElement(aux.getPid(),aux.getEstado())
            print("Actualizacion realizada con exito.")

    def __updateElement(self, pid, estado):
        db = TinyDB('db.json')
        db.update({"estado": estado, "ultMod": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}, Query().pid == pid)


    def eliminarTarea(self, pid):
        aux = True
        for x in self.listaDeTareas:
            if(pid == x.getPid()):
                aux = False
                self.__deleteElement(x.getPid())
                self.listaDeTareas.remove(x)
                print("Eliminacion realizada con exito.")
        
        if(aux):
            raise Exception(f"El id {pid} no se encuentra en la lista de tareas.")

    def __deleteElement(self, pid):
        db = TinyDB('db.json')
        db.remove(Query().pid == pid)
                #self.__cargarLista()

    def taskList(self)->list:
        return self.listaDeTareas
    
    def __cargarLista(self):
        db = TinyDB('db.json')
        result = db.all()
        if(len(result)):
            for x in result:
                self.listaDeTareas.append(Task(**x))
        else:
            print("Lista vacía")
        

    def __insertarTarea(self, tarea):
        db = TinyDB('db.json')
        print(tarea.toDic())
        db.insert(tarea.toDic())

"""
    def __updateElement(self, element):
        db = TinyDB('db.json')
        tarea = None
        for x in self.listaDeTareas:
            if(element.getPid()):
                tarea = x

        if(tarea == None):
            raise Exception(f"El id {element.getPid()} no se encuentra en la lista de tareas.")

        if(element.getNombre() != ""):
            db.update({'nombre': element.getNombre(), "ultMod": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}, Query().pid == tarea.getPid())
        if(element.getEstado() != 0):
            db.update({"estado": element.getEstado(), "ultMod": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}, Query().pid == tarea.getPid())
"""