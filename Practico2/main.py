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
