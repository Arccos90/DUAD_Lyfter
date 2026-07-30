print("-------------------------Exercise_2---------------------------")
import csv
import os


def input_game ():
    temporal_list = []
    while True:
        temporal_dicc = {}
        name = input(f"Ingrese el nombre del videojuego:")
        gender = input(f"Ingrese el genero del video juego:")
        developer = input(f"Ingrese el nombre del desarrollador del video juego: ")
        class_ESRB = input(f"Ingrese la clasificación ESRB del video juego: ")
        temporal_dicc['Nombre'] = name
        temporal_dicc['Género'] = gender
        temporal_dicc['Desarrollador'] = developer
        temporal_dicc[ 'Clasificación ESRB'] = class_ESRB
        print (temporal_dicc)
        print ("Desea ingresar otro video juego")
        temporal_list.append(temporal_dicc)
        menu_option = input(f"S/N :")
        if menu_option == "S":
            continue
        elif menu_option == "N":
            break
    print (temporal_list)
    return temporal_list


def write_on_file (file_path, data):
    with open (file_path,'w', encoding='utf-8', newline="") as file:
        headers = data [0].keys()
        writer = csv.DictWriter(file,fieldnames=headers, delimiter= "\t") #Acá se modifica para que ahora use tabulacion en lugar de la coma
        writer.writeheader()
        writer.writerows(data)


def append_on_file (file_path, data):
    with open(file_path, 'a', encoding='utf-8', newline="") as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t")
        writer.writerows(data)


def read_file(file_path):
    try:
        counter = 0
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t") # acá se modifica el separador para que lea tabulacion en lugar de la coma
            for game in reader:
                counter = counter + 1
                print (game)
            print(f"!Hay {counter} juego(s) ingresado(s)!")
        return counter
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return 0 # Si no existe el archivo brinca hasta el except y no retorna ningún valor, por lo que genera un error en la formula main()


def main():
    while True:
        print("--------------------------Menú Principal-------------------------------")
        print("1- Mostrar los datos del archivo")
        print("2- Ingresar un nuevo registro")
        print("3- Salir")
        main_menu_option = int(input(f"Ingrese una opcion: "))
        ruta_terminal = os.path.dirname(os.path.abspath(__file__))+"/games_input_exc2.csv"
        
        if main_menu_option == 1:
            print("-------------------------------Resultado------------------------------")
            counter_value = read_file(ruta_terminal)
            continue
            
        if main_menu_option == 2:
            counter_value = read_file(ruta_terminal)
            data_input = input_game ()
            if counter_value >= 1:
                append_on_file (ruta_terminal,data_input)
            elif counter_value == 0:
                write_on_file (ruta_terminal, data_input)
            continue
        if main_menu_option == 3:
            print("Cerrando el programa........... Nos vemos pronto!")
            break
main()