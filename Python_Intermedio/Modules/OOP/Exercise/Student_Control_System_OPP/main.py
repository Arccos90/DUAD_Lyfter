import os
import menu
import actions
import data

def main():
    terminal_route = os.path.dirname(os.path.abspath(__file__)) + "/Student_BD.csv"
    student_session_list = []
    
    while True:
        menu.display_menu()
        try:
            main_menu_option = int(input("Por favor ingrese una opción: "))
        except ValueError:
            print("!Error! Debe ingresar un número entero")
            continue

        if main_menu_option == 1:
            while True:
                print("-------------------INGRESE UN NUEVO ESTUDIANTE------------------------")
                student_data = actions.input_new_data(student_session_list)
                student_session_list.append(student_data)
                print(f"¡Estudiante {student_data.student_name} agregado exitosamente!")
                
                print("¿Desea ingresar otro estudiante?")
                menu_option = input("S/N: ").strip().upper()
                if menu_option == "N":
                    break
            continue

        elif main_menu_option == 2:  
            print("-------------------REPORTE ESTUDIANTES INGRESADOS-----------------------")
            if not student_session_list:
                print("No hay estudiantes registrados en la sesión actual.")
            else:
                for index, student in enumerate(student_session_list, start=1):
                    # Acceso mediante atributos de la clase Student
                    print(f"{index}...ID: {student.id} --Nombre: {student.student_name} {student.last_name} {student.second_surname} ___ Sección: {student.type}")
            
            next_option = input("\n¿Desea continuar en el menú? <S/N>: ").strip().upper()
            if next_option == "N":
                menu.bye_banner()
                break

        elif main_menu_option == 3:
            print("-------------------REPORTE NOTAS TOP 3------------------------")
            data.avg_sort_temporary_file(student_session_list)
            next_option = input("\n¿Desea continuar en el menú? <S/N>: ").strip().upper()
            if next_option == "N":
                menu.bye_banner()
                break

        elif main_menu_option == 4:
            print("-------------------REPORTE DE NOTAS PROMEDIO POR ESTUDIANTE------------------------")
            data.avg_read_temporary_file(student_session_list)
            next_option = input("\n¿Desea continuar en el menú? <S/N>: ").strip().upper()
            if next_option == "N":
                menu.bye_banner()
                break

        elif main_menu_option == 5:
            print("\nExportando datos a CSV...")
            data.write_on_file(terminal_route, student_session_list)
            next_option = input("\n¿Desea continuar en el menú? <S/N>: ").strip().upper()
            if next_option == "N":
                menu.bye_banner()
                break

        elif main_menu_option == 6:
            print("\nImportando datos desde CSV...")
            saved_student = data.read_file(terminal_route)
            student_session_list.extend(saved_student)
            next_option = input("\n¿Desea continuar en el menú? <S/N>: ").strip().upper()
            if next_option == "N":
                menu.bye_banner()
                break

        elif main_menu_option == 7:
            print("-------------------REPORTE DE NOTAS PROMEDIO GENERAL-----------------------")
            data.avg_total_temporary_file(student_session_list)
            next_option = input("\n¿Desea continuar en el menú? <S/N>: ").strip().upper()
            if next_option == "N":
                menu.bye_banner()
                break

        elif main_menu_option == 8:
            menu.bye_banner()
            break

        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 8.")

if __name__ == "__main__":
    main()