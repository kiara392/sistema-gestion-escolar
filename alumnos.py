def agregar_alumno(datos):
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    dni = input("Ingrese el dni del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
    tutor = input("Ingrese nombre y apellido del tutor: ")


    alumno = {"Nombre":nombre, "Apellido": apellido, "DNI": dni, "Fecha de nacimiento": fecha_nacimiento,"Tutor": tutor,
              "Notas": [], "Faltas": 0, "Amonestaciones": 0} 

    datos["Alumnos"].append(alumno)

    print("Alumno agregado correctamente.")

def mostrar_alumno(alumno):
    print("=====================================")
    print("Nombre: ", alumno["Nombre"])
    print("Apellido: ", alumno["Apellido"])
    print("DNI: ", alumno["DNI"])
    print("Fecha de nacimiento: ", alumno["Fecha de nacimiento"])
    print("Tutor: ", alumno["Tutor"])
    print("Notas: ", alumno["Notas"])
    print("Faltas: ", alumno["Faltas"])
    print("Amonestaciones: ", alumno["Amonestaciones"])
    print("=====================================")


def mostrar_alumnos(datos):
    if len(datos["Alumnos"]) == 0:
        print("No hay alumnos registrados.")
        return

    for alumno in datos["Alumnos"]:
        mostrar_alumno(alumno)



def buscar_alumno(datos):
    dni_buscado = input("Ingrese el DNI del alumno que desea buscar: ")

    for alumno in datos["Alumnos"]:

        if alumno["DNI"] == dni_buscado:
            print("Alumno encontrado.")
            mostrar_alumno(alumno)
            return


    print("No se encontro un alumno con ese DNI.")


def modificar_alumno(datos):
    dni_buscado = input("Ingrese el DNI del alumno que desea modificar: ")

    for alumno in datos["Alumnos"]:
        if alumno["DNI"] == dni_buscado:

            print("Alumno encontrado.")

            while True:
                print()
                print("1. Nombre")
                print("2. Apellido")
                print("3. DNI")
                print("4. Fecha de nacimiento")
                print("5. Tutor")
                print("6. Faltas")
                print("7. Amonestaciones")
                print("8. Notas")
                print("9. Salir al menu principal")

                opcion = input("Ingrese la opcion que desea modificar: ")

                if opcion == "1":
                    alumno["Nombre"] = input("Ingrese el nuevo nombre: ")

                elif opcion == "2":
                    alumno["Apellido"] = input("Ingrese el nuevo apellido: ")

                elif opcion == "3":
                    alumno["DNI"] = input("Ingrese el nuevo DNI: ")

                elif opcion == "4":
                    alumno["Fecha de nacimiento"] = input("Ingrese la nueva fecha de nacimiento: ")

                elif opcion == "5":
                    alumno["Tutor"] = input("Ingrese el nuevo tutor: ")

                elif opcion == "6":
                    alumno["Faltas"] = int(input("Ingrese la cantidad de faltas"))

                elif opcion == "7":
                    alumno["Amonestaciones"] = int(input("Ingrese la cantidad de amonestaciones: "))

                elif opcion == "8":
                    nota = float(input("Ingrese la nota: "))
                    alumno["Notas"].append(nota)
                elif opcion == "9":
                    return

                else:
                    print("Opcion incorrecta.")
                    

    print("Datos modificados correctamente.")
        

    print("No se encontro un alumno con ese DNI.")


def expulsar_alumno(datos):
    dni_buscado = input("Ingrese el DNI del alumno que desea expulsar: ")

    for alumno in datos["Alumnos"]:

        if alumno["DNI"] == dni_buscado:

            print("Alumno encontrado: ")
            print(alumno["Nombre"], alumno["Apellido"])

            confirmacion = input("¿Esta seguro que desea expulsar al alumno? (si/no:)")

            if confirmacion.lower() == "si":
                datos["Alumnos"].remove(alumno)
                print("Alumno expulsado correctamente.")
            else:
                print("Operacion cancelada.")

            return

    print("No se encontro un alumno con ese DNI.")


