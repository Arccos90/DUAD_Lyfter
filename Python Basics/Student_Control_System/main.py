import os
import menu
import actions
import data

def main ():
    terminal_route = os.path.dirname(os.path.abspath(__file__))+"/Student_BD.csv"
    student_session_list = []
    print(terminal_route)
    
    while True:
            menu.display_menu()
            try:
                main_menu_option= int(input(f"Por favor ingrese una opción:"))
            except ValueError:
                print("!Error! Debe ingresar un número entero")
                continue
            if main_menu_option == 1:
                while True:
                    print("-------------------INGRESE UN NUEVO ESTUDIANTE------------------------")
                    student_data= actions.input_new_data(student_session_list)
                    student_session_list.append(student_data)
                    print(student_session_list)
                    print ("Desea ingresar otro estudiante?")
                    menu_option = input(f"S/N :").upper()
                    if menu_option == "N":
                        break
                continue

            elif main_menu_option == 2:  
                print("-------------------REPORTE ESTUDIANTES INGRESADOS-----------------------")
                for index, student in enumerate (student_session_list, start=1):
                    print(f"{index}...ID: {student['ID']} --Nombre: {student['student_name']} {student['last_name']} {student['second_surname']}___ Sección: {student['type']}")
                next_option=input("Desea continuar? <S/N>: ").upper()
                if next_option == "N":
                    break
                elif next_option == "S":
                    continue
            elif main_menu_option == 3:

                print("-------------------REPORTE NOTAS TOP 3------------------------")
                data.avg_sort_temporary_file(student_session_list)
                next_option=input("Desea continuar? <S/N>: ").upper()
                if next_option == "N":
                    break
                elif next_option == "S":
                    continue
            elif main_menu_option == 4:
                print("-------------------REPORTE DE NOTAS PROMEDIO POR ESTUDIANTE------------------------")
                data.avg_read_temporary_file(student_session_list)
                next_option=input("Desea continuar? <S/N>: ").upper()
                if next_option == "S":
                    continue
                else:
                    break
            elif main_menu_option == 5:
                print("Exportando------------------------")
                data.write_on_file(terminal_route,student_session_list)
                next_option=input("Desea continuar? <S/N>: ").upper()
                if next_option == "S":
                    continue
                else:
                    break

            elif main_menu_option == 6:
                print("Importando------------------------")
                saved_student=data.read_file(terminal_route)
                student_session_list.extend(saved_student)
                next_option=input("Desea continuar? <S/N>: ").upper()
                if next_option == "S":
                    continue
                else:
                    break

            elif main_menu_option == 7:
                print("-------------------REPORTE DE NOTAS PROMEDIO GENERAL-----------------------")
                data.avg_total_temporary_file(student_session_list)
                next_option=input("Desea continuar? <S/N>: ").upper()
                if next_option == "S":
                    menu.display_menu()
                    continue
                else:
                    break
            elif main_menu_option == 8:
                menu.bye_banner()
    
                break
            else:
                print("Option Failure. Please enter a number between 1 to 6.")

if __name__ == "__main__":
    main()    