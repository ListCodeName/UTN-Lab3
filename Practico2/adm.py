"""
agregar_tarea(tarea: Tarea) -> int: Agrega una nueva tarea a la base de datos y devuelve su ID.
traer_tarea(tarea_id: int) -> Task: Obtiene una tarea de la base de datos según su ID y devuelve una instancia de la clase Tarea.
actualizar_estado_tarea(tarea_id: int, estado: str): Actualiza el estado de una tarea en la base de datos según su ID.
eliminar_tarea(tarea_id: int): Elimina una tarea de la base de datos según su ID.
traer_todas_tareas() -> List[Tarea]: Obtiene todas las tareas de la base de datos y devuelve una lista de instancias de la clase Task.
"""
from task import Task
import random
class Admin:
    listaDeTareas = []

    def __init__(self):
        pass

    def addTask(self, nombre):
        nuevoPid = 1
        flag = True
        while(flag):
            flag = False
            for x in self.listaDeTareas:
                if( nuevoPid == Task(x).getPid()):
                    nuevoPid = random.randint(1,1000)
                    flag = True
                    break
        self.listaDeTareas.append(Task(nombre, nuevoPid))
            
    def getTask(self, pid)->Task:
        for x in self.listaDeTareas:
            if(pid == Task(x).getPid()):
                return x

    def statusUpdate(self, pid, estado)->Exception:
        aux = None
        for x in self.listaDeTareas:
            if( pid == Task(x).getPid()):
                aux = x
                break
        if(aux == None):
            raise Exception("Elemento no encontrado.")
        else:
            Task(aux).cambiarEstado(estado)
            self.__updateElement(aux)


    def eliminarTarea(self, pid):
        for x in self.listaDeTareas:
            if(pid == Task(x).getPid()):
                self.__deleteElement(x)
                self.listaDeTareas.remove(x)


    def taskList(self):
        return self.listaDeTareas
    
    def __cargarLista(self):
        pass #tinidb cargar elementos a la lista

    def __deleteElement(self, element):
        pass #tinidb eliminar elemento

    def __updateElement(self, element):
        pass #tinidb actualizar