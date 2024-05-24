#Funcion: agregar_tarea(lista, descripcion) 
#Añade una nueva tarea (representada como un diccionario) a la lista.
def agregar_tarea(lista, descripcion):
    tarea = {"descripcion": descripcion, "completada": False}      #carga variable tarea con el nuevo diccionario creado con valor FALSE por defecto 
    lista.append(tarea)                                            #agrega mi diccionario a la lista

#Funcion: marcar_tarea_completada(lista, posicion) 
#Marca una tarea específica como completada. Maneja excepciones si la posición es inválida.
def marcar_tarea_completada(lista, posicion):
    try:
        lista[posicion]["completada"] = True                       #Cambia el valor del campo compeltada a TRUE
    except IndexError:
        print("Error: La posición ingresada no es válida.")        #la posición es inválida.

#Funcion: mostrar_tareas(lista)
#Muestra todas las tareas con sus estados (completada o pendiente).
def mostrar_tareas(lista):
    if not lista:
        print("No hay tareas para mostrar.")
    else:
        #recorre las tareas enumerandolas en su impresion
        for i, tarea in enumerate(lista):  
            estado = "Completada" if tarea["completada"] else "Pendiente"  #cargo mi variable estado con el valor (completada o pendiente)
            print(f"{i + 1}. {tarea['descripcion']} - {estado}")           #imprime en pantalla las tareas y su estado

#Funcion: eliminar_tarea(lista, posicion) 
#Elimina una tarea específica de la lista. Maneja excepcion si la posición es inválida.
def eliminar_tarea(lista, posicion):
    try:
        del lista[posicion]
    except IndexError:
        print("Error: La posición ingresada no es válida.") #posición es inválida


#funcion: main()
#Proporciona una interfaz de usuario para interactuar con las tareas.
#Permite al usuario seleccionar opciones para agregar, marcar como completada, mostrar o eliminar tareas.
#Maneja excepciones para entradas no válidas y asegura que el programa no se cierre inesperadamente.
def main():
    lista_de_tareas = []                                                 #Crea la lista en donde se almacenaran los diccionarios (tareas)

    while True:                                                         # Imprime las opciones para interactuar con las tareas
        print("\nGestor de Tareas Pendientes")
        print("1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")

        try:                                                         
            opcion = int(input("Elija una opción: "))                  # Imprime y solicita el ingreso de la opción
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")       
            continue
            
        # Evalua la opcion ingresada
        if opcion == 1:
            descripcion = input("Ingrese la descripción de la tarea: ")
            agregar_tarea(lista_de_tareas, descripcion)
        elif opcion == 2:
            try:
                posicion = int(input("Ingrese la posición de la tarea a marcar como completada: ")) - 1
                marcar_tarea_completada(lista_de_tareas, posicion)
            except ValueError:                                               #Maneja excepcion si la posición es inválida.
                print("Error: Por favor, ingrese un número válido.")
        elif opcion == 3:
            mostrar_tareas(lista_de_tareas)
        elif opcion == 4:
            try:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1 #resta 1 a la posicion para la ubicacion del indice.
                eliminar_tarea(lista_de_tareas, posicion)
            except ValueError:                                               #Maneja excepcion si la posición es inválida.
                print("Error: Por favor, ingrese un número válido.")
        elif opcion == 5:                                                    #Sale del bucle
            break
        else:
            print("Error: Opción no válida. Por favor, elija una opción del 1 al 5.")
            
#Ejecuta funcion de inicio
if __name__ == "__main__":
    main()
