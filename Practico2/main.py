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
    administrador.addTask(input("Nombre de la tarea: "), input("Añada una descripción: "))

def actualizarTarea(administrador):
    print("\n-------------- Actualizar tarea ----------------")
    while(True):
        try:
            administrador.statusUpdate(int(input("Escriba el id: ")), input("Estado (1,0,-1): "), input("**Ingrese nuevo nombre: "), input("**Ingrese descripción: "))
            break
        except Exception as e:
            print(e, "\n")

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