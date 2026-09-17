"-------------------------------------Actions--------------------------------------------------"
import data
import os

def input_new_data ():
    terminal_route = os.path.dirname(os.path.abspath(__file__))+"/Student_BD.csv"
    ID_counter = data.counter_data_on_file(terminal_route)
    Temporal_new_student = []
    counter = ID_counter
    new_student = {}
    while True:
        print("----------------Por favor, Ingrese la información del estudiante-------------------")
        name = str(input(f"Por favor ingrese el nombre:")).upper()
        last_name = str(input(f"Por favor ingrese el apellido:")).upper()
        second_surname= str(input(f"Por favor ingrese el segundo apellido:")).upper()
        class_id = str(input(f"Por favor ingrese la sección: ")).upper()
        counter = counter +1
        while True:
            spanish_note= float(input(f"Por favor ingrese la nota de Español: "))
            if 0 <= spanish_note <= 100: 
                print ("Nota ingresada")
                break
            else:
                print("!por favor ingrese un valor entre 0 y 100!")

        while True:
            english_note = float(input(f"Por favor ingrese la nota de Ingles: "))
            if 0<= english_note <= 100 :
                print ("Nota ingresada")
                break
            else:
                print("!por favor ingrese un valor entre 0 y 100!")
        while True:        
            socials_note = float(input(f"Por favor ingrese la nota de Sociales: "))
            if 0<= socials_note <= 100:
                print("Nota ingresada")
                break
            else:
                print("!por favor ingrese un valor entre 0 y 100!")
        while True:        
            science_note= float(input(f"Por favor ingrese la nota de Ciencias: "))
            if 0<= science_note <=100:
                print("Nota ingresada")
                break
            else:
                print("!por favor ingrese un valor entre 0 y 100!")
        avg_note = (spanish_note+english_note + socials_note + science_note) / 4
        new_student = {
            'ID': counter,
            'student_name': name,
            'last_name': last_name,
            'second_surname': second_surname,
            'type': class_id,
            'spanish': spanish_note,
            'english': english_note,
            'socials':socials_note,
            'science': science_note,
            'avg_note': avg_note
        }
        Temporal_new_student.append(new_student)
        print (Temporal_new_student)
        print ("Desea ingresar otro estudiante?")
        menu_option = input(f"S/N :").upper()
        if menu_option == "S":
            counter = counter+1
            continue
        elif menu_option == "N":
            return Temporal_new_student

def save_input_new_data (student_list):
    print(student_list)
    return student_list


