print("--------------------------Exercise_#4: Files Management--------------------------------")
import os

def write_new_line (path):
    new_line = input(f"Ingrese el texto que desea agregar en el archivo: ")
    try:    
        with open(path, 'a', encoding='utf-8') as file:
            file.write("\n" + new_line)
            print()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {path}, se ha creado un nuevo archivo")


def read_files_by_lines (path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read()
        print (lines)
    

def main():
    ruta_terminal = os.path.dirname(os.path.abspath(__file__))+"/Text_input_exc4.txt"
    write_new_line (ruta_terminal)
    print("---------------información ha sido guardada-----------------")
    read_files_by_lines (ruta_terminal)


main()