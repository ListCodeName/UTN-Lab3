"""
Crear una aplicación de línea de comandos para administrar una lista de tareas.

La aplicación permitirá al usuario agregar, ver, actualizar y eliminar tareas.

Requisitos:

Utiliza TinyDB para almacenar las tareas en una base de datos.

Crea una clase Tarea que tenga las siguientes propiedades: id, titulo, descripción, estado, creada y actualizada.

Crea una clase Administrador de Tareas (AdminTarea) que maneje la interacción con la base de datos TinyDB. La clase debe tener los siguientes métodos:

agregar_tarea(tarea: Tarea) -> int: Agrega una nueva tarea a la base de datos y devuelve su ID.
traer_tarea(tarea_id: int) -> Task: Obtiene una tarea de la base de datos según su ID y devuelve una instancia de la clase Tarea.
actualizar_estado_tarea(tarea_id: int, estado: str): Actualiza el estado de una tarea en la base de datos según su ID.
eliminar_tarea(tarea_id: int): Elimina una tarea de la base de datos según su ID.
traer_todas_tareas() -> List[Tarea]: Obtiene todas las tareas de la base de datos y devuelve una lista de instancias de la clase Task.
"""

from adm import Admin
from task import Task

def listarTareas(listado):
    print("\n-------------- Lista de tareas ----------------")
    if(len(listado)):
        for x in range (0,len(listado)):
            print(listado[x])
    else:
        print("No se encontraron elementos.")


def agregarTarea(administrador):
    print("\n-------------- Agregar tarea ----------------")
    administrador.addTask(input("Nombre de la tarea: "))

def actualizarTarea(administrador):
    print("\n-------------- Actualizar tarea ----------------")
    try:
        administrador.statusUpdate(int(input("Escriba el id: ")),int(input("Estado (1,0,-1): ")))
    except Exception as e:
        print(e)

def eliminarTarea(administrador):
    print("\n-------------- Eliminar tarea ----------------")
    try:
        administrador.eliminarTarea(int(input("Escriba el id: ")))
    except Exception as e:
        print(e)

adm = Admin()
flag = True
while(flag):
    print("\n---------- Menu ------------")
    print("[1] Listar las tareas.")
    print("[2] Agregar una tarea.")
    print("[3] Actualizar estado de una tarea.")
    print("[4] Eliminar una tarea.")
    print("[0] Salir")
    flag = int(input(">>>"))
    if(flag == 1):
        listarTareas(adm.taskList())
    elif(flag == 2):
        agregarTarea(adm)
    elif(flag == 3):
        actualizarTarea(adm)
    elif(flag == 4):
        eliminarTarea(adm)