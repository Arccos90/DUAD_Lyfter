"-------------------------------------Actions--------------------------------------------------"
import os
import data
from Student import Student

def input_new_data(temporary_file):
    terminal_route = os.path.dirname(os.path.abspath(__file__)) + "/Student_BD.csv"
    ID_counter = data.counter_data_on_file(terminal_route)
    counter = ID_counter + len(temporary_file) + 1

    print("----------------Por favor, Ingrese la información del estudiante-------------------")
    name = str(input("Por favor ingrese el nombre: ")).upper().strip()
    last_name = str(input("Por favor ingrese el apellido: ")).upper().strip()
    second_surname = str(input("Por favor ingrese el segundo apellido: ")).upper().strip()
    class_id = str(input("Por favor ingrese la sección: ")).upper().strip()

    while True:
        try:
            spanish_note = float(input("Por favor ingrese la nota de Español: "))
            if 0 <= spanish_note <= 100:
                print("Nota ingresada")
                break
            print("!Por favor ingrese un valor entre 0 y 100!")
        except ValueError:
            print("!Error! Por favor ingrese un número válido")

    while True:
        try:
            english_note = float(input("Por favor ingrese la nota de Ingles: "))
            if 0 <= english_note <= 100:
                print("Nota ingresada")
                break
            print("!Por favor ingrese un valor entre 0 y 100!")
        except ValueError:
            print("!Error! Por favor ingrese un número válido")

    while True:
        try:
            socials_note = float(input("Por favor ingrese la nota de Sociales: "))
            if 0 <= socials_note <= 100:
                print("Nota ingresada")
                break
            print("!Por favor ingrese un valor entre 0 y 100!")
        except ValueError:
            print("!Error! Por favor ingrese un número válido")

    while True:
        try:
            science_note = float(input("Por favor ingrese la nota de Ciencias: "))
            if 0 <= science_note <= 100:
                print("Nota ingresada")
                break
            print("!Por favor ingrese un valor entre 0 y 100!")
        except ValueError:
            print("!Error! Por favor ingrese un número válido")

    # Retorna directamente el objeto Student
    return Student(
        id_student=counter,
        student_name=name,
        last_name=last_name,
        second_surname=second_surname,
        class_type=class_id,
        spanish=spanish_note,
        english=english_note,
        socials=socials_note,
        science=science_note
    )