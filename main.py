from datos import datos

from alumnos import (agregar_alumno, mostrar_alumnos, buscar_alumno,
                     modificar_alumno, expulsar_alumno)



def menu():
    while True:

        print()
        print("=== SISTEMA DE GESTION ESCOLAR===")
        print("1. Agregar alumno")
        print("2. Mostrar alumno")
        print("3. Buscar alumno")
        print("4. Modificara alumno")
        print("5. Expulsar alumno")
        print("6. Salir")
        print()


        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            agregar_alumno(datos)

        elif opcion == "2":
            mostrar_alumnos(datos)

        elif opcion == "3":
            buscar_alumno(datos)

        elif opcion == "4":
            modificar_alumno(datos)

        elif opcion == "5":
            expulsar_alumno(datos)

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opcion incorrecta.")

menu()