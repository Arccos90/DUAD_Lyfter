import os
import menu
import actions
import data

def main ():
    terminal_route = os.path.dirname(os.path.abspath(__file__))+"/Student_BD.csv"
    print(terminal_route)
    while True:
            menu.display_menu()
            main_menu_option= int(input(f"Por favor ingrese una opción:"))
            if main_menu_option == 1:
                print("-------------------INGRESE UN NUEVO ESTUDIANTE------------------------")
                student_data= actions.input_new_data()
                final_data_ready = actions.save_input_new_data (student_data)
                next_option= input("Desea guardar la informacion? <S/N>:").upper()
                if next_option == "S":
                    if data.counter_data_on_file(terminal_route)==0:
                        print (data.counter_data_on_file(terminal_route))
                        data.write_on_file(terminal_route,final_data_ready)
                    elif data.counter_data_on_file(terminal_route)>=0:
                        print (data.counter_data_on_file(terminal_route))
                        data.append_on_file(terminal_route,final_data_ready)
                elif next_option == "N":
                    continue
            elif main_menu_option == 5:
                print("-------------------BUSQUEDA POR NOMBRE DE ESTUDIANTE------------------------")
                #new_pokemon_info = input_new_data()
                #append_on_json_file (terminal_route, new_pokemon_info)
                next_option=input("Desea continuar? <S/N>: ").upper()
                if next_option == "S":
                    menu.display_menu()
                    continue
                else:
                    break
    
            elif main_menu_option == 2:  
                print("-------------------REPORTE ESTUDIANTES INGRESADOS-----------------------")
                #report_by_type(terminal_route)
                data.read_file(terminal_route)
                next_option=input("Desea continuar? <S/N>: ").upper()
                if next_option == "N":
                    break
                elif next_option == "S":
                    continue
            elif main_menu_option == 3:
                print("-------------------REPORTE NOTAS TOP 3------------------------")
                data.avg_sort_read_file(terminal_route)
                next_option=input("Desea continuar? <S/N>: ").upper()
                if next_option == "N":
                    break
                elif next_option == "S":
                    continue
            elif main_menu_option == 4:
                print("-------------------REPORTE DE NOTAS PROMEDIO POR ESTUDIANTE------------------------")
                data.avg_read_file(terminal_route)
                next_option=input("Desea continuar? <S/N>: ").upper()
                if next_option == "S":
                    continue
                else:
                    break
            elif main_menu_option == 6:
                menu.bye_banner()
    
                break
            else:
                print("Option Failure. Please enter a number between 1 to 6.")

if __name__ == "__main__":
    main()    