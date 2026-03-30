# GESTOR DE TAREAS COMPLETO

# Función para agregar una tarea
def agregar_tarea(tareas, descripcion, fecha_limite, prioridad, completada=False):
    # Creamos un diccionario con los datos de la tarea
    tarea = {
        "descripcion": descripcion,
        "fecha": fecha_limite,
        "prioridad": prioridad,
        "completada": completada  # Por defecto es False
    }

    # Agregamos la tarea a la lista
    tareas.append(tarea)

    print("✅ Tarea agregada correctamente")


# Función para mostrar tareas
def mostrar_tareas(tareas, completadas=None):
    # Si no hay tareas
    if not tareas:
        print("⚠ No hay tareas cargadas.")
        return

    print("\n📋 LISTA DE TAREAS:")

    # Recorremos la lista con índice
    for i, t in enumerate(tareas, 1):

        # Filtro según parámetro completadas
        if completadas == True and not t["completada"]:
            continue  # salta tareas no completadas

        if completadas == False and t["completada"]:
            continue  # salta tareas completadas

        # Estado de la tarea
        estado = "✔ Completada" if t["completada"] else "✘ Pendiente"

        # Mostramos la tarea
        print(f"\nTarea {i}:")
        print("Descripción:", t["descripcion"])
        print("Fecha límite:", t["fecha"])
        print("Prioridad:", t["prioridad"])
        print("Estado:", estado)


# Función para marcar tarea como completada
def marcar_completada(tareas):
    # Verificamos que haya tareas
    if not tareas:
        print("⚠ No hay tareas para completar.")
        return

    # Mostramos todas las tareas
    mostrar_tareas(tareas)

    try:
        # Pedimos número de tarea
        indice = int(input("\nNúmero de tarea a completar: ")) - 1

        # Verificamos si el índice es válido
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            print("✅ Tarea marcada como completada")
        else:
            print("❌ Índice inválido")

    except ValueError:
        print("❌ Debes ingresar un número válido")


# PROGRAMA PRINCIPAL

# Este bloque asegura que el código solo se ejecute
# cuando el archivo se corre directamente
if __name__ == "__main__":

    # Lista donde se guardan las tareas
    lista_tareas = []

    # Bucle principal del programa
    while True:

        # Mostramos menú
        print("\n====== MENÚ ======")
        print("1. Agregar tarea")
        print("2. Mostrar TODAS las tareas")
        print("3. Mostrar tareas COMPLETADAS")
        print("4. Mostrar tareas PENDIENTES")
        print("5. Marcar tarea como completada")
        print("6. Salir")

        # Pedimos opción
        opcion = input("Elegí una opción: ")

    # OPCIÓN 1: AGREGAR TAREA
        if opcion == "1":
            descripcion = input("Descripción: ")
            fecha = input("Fecha límite: ")
            prioridad = input("Prioridad (alta/media/baja): ")

            # Llamamos a la función
            agregar_tarea(lista_tareas, descripcion, fecha, prioridad)

        # OPCIÓN 2: MOSTRAR TODAS
        elif opcion == "2":
            mostrar_tareas(lista_tareas)

        # OPCIÓN 3: SOLO COMPLETADAS
        elif opcion == "3":
            mostrar_tareas(lista_tareas, completadas=True)

        # OPCIÓN 4: SOLO PENDIENTES
        elif opcion == "4":
            mostrar_tareas(lista_tareas, completadas=False)

        # OPCIÓN 5: MARCAR COMPLETADA
        elif opcion == "5":
            marcar_completada(lista_tareas)

        # OPCIÓN 6: SALIR
        elif opcion == "6":
            print("👋 Saliendo del programa...")
            break

        # OPCIÓN INVÁLIDA
        else:
            print("❌ Opción inválida. Intentá de nuevo.")