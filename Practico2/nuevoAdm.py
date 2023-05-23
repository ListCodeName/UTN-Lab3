from task import Task
import random, datetime
from tinydb import TinyDB, Query

class Admin:
    def __init__(self):
        self.listaDeTareas = []
        self.__cargarLista()
        
    #Añadir tarea
    def addTask(self, nombre, descripcion):
        nuevoPid = 1
        flag = True
        while(flag):
            flag = False
            if(len(self.listaDeTareas)!= 0):
                for x in self.listaDeTareas:
                    if( nuevoPid == x.getPid()):
                        nuevoPid = random.randint(1,1000)
                        flag = True
                        break
        nuevaTarea = Task(nuevoPid, nombre, descripcion, None, None, None)
        self.listaDeTareas.append(nuevaTarea)
        #self.__insertarTarea(nuevaTarea)
        
    def __insertarTarea(self, tarea):
        db = TinyDB('db.json')
        print(tarea.toDic())
        db.insert(tarea.toDic())





    #Obtener una tarea
    def getTask(self, pid)->Task:
        for x in self.listaDeTareas:
            if(pid == Task(x).getPid()):
                return x





    #Actualizar tareas
    def statusUpdate(self, pid, estado, nombre, descripcion):
        aux = None
        for x in self.listaDeTareas:
            if( pid == x.getPid()):
                aux = x
                break
        if(aux == None):
            raise Exception(f"El id {pid} no se encuentra en la lista de tareas.")
        else:
            if(estado != None or estado != ""):
                try:
                    aux.cambiarEstado(int(estado))
                except Exception as e:
                    raise Exception(e)
            if(nombre != None or nombre != ""):
                aux.setNombre(nombre)
            if(descripcion != None or descripcion != ""):
                aux.setDescripcion(descripcion)
    #        self.__updateElementStatus(aux.getPid(),aux.getEstado())
            print("Actualizacion realizada con exito.")

    def __updateElementStatus(self, pid, estado):
        db = TinyDB('db.json')
        db.update({"estado": estado, "ultMod": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}, Query().pid == pid)

    



    #Eliminar tarea

    def eliminarTarea(self, pid):
        aux = True
        for x in self.listaDeTareas:
            if(pid == x.getPid()):
                aux = False
                #self.__deleteElement(x.getPid())
                self.listaDeTareas.remove(x)
                print("Eliminacion realizada con exito.")
        
        if(aux):
            raise Exception(f"El id {pid} no se encuentra en la lista de tareas.")

    def __deleteElement(self, pid):
        db = TinyDB('db.json')
        db.remove(Query().pid == pid)
                #self.__cargarLista()




    #Listar tareas

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
    