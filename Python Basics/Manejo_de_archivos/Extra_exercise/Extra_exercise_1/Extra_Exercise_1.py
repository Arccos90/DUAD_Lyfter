print("--------------------------Exercise_#1: Files Management--------------------------------")
import os

def read_files_by_lines (path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().replace("\n"," ")
        print (lines)
    return lines


def write_new_files_by_lines (new_path,my_line):
    with open (new_path,'w', encoding='utf-8') as file:
        file.write(my_line)


def main():    
    ruta_terminal = os.path.dirname(os.path.abspath(__file__))+"/Text_input_exc1.txt"
    new_route_terminal = os.path.dirname(os.path.abspath(__file__))+"/Text_input2_exc1.txt"
    new_line = read_files_by_lines(ruta_terminal)
    write_new_files_by_lines (new_route_terminal,new_line)


main()