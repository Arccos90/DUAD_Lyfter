print("-------------------------Extra_exercise_2------------------------")
import csv
import os


def input_game ():
    temporal_list = []
    while True:
        temporal_dicc = {}
        name = input(f"Ingrese el nombre del videojuego:")
        genre = input(f"Ingrese el genero del video juego:")
        developer = input(f"Ingrese el nombre del desarrollador del video juego: ")
        class_ESRB = input(f"Ingrese la clasificación ESRB del video juego: ")
        temporal_dicc['Name'] = name
        temporal_dicc['Genre'] = genre
        temporal_dicc['Developer'] = developer
        temporal_dicc[ 'ESRB rating'] = class_ESRB
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
        writer = csv.DictWriter(file,fieldnames=headers, delimiter="\t")
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
            reader = csv.DictReader(file, delimiter="\t")
            for game in reader:
                counter = counter + 1
                #Acá vamos a trabajar el reporte de todos los juegos ingresados de manera ordenada.
                print(f"Juego {counter}")
                print(f"  - Name:            {game['Name']}")
                print(f"  - Genre:           {game['Genre']}")
                print(f"  - Developer:       {game['Developer']}")
                print(f"  - ESRB Rating:     {game['ESRB rating']}")
                print("-"*50)
            print(f"!Hay {counter} juego(s) ingresado(s)!")
            print("-"*50)
        return counter
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return 0 # Si no existe el archivo brinca hasta el except y no retorna ningún valor, por lo que genera un error en la formula main()


def report_file_by_rating(file_path):
    try:
        counter = 0

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            filter_header = input(f"Ingrese la clasificación ESRB: ")
            print (f"...................Juegos con la categoría ESRB {filter_header.upper()}................")
            for game in reader:
                if game ['ESRB rating'].lower() == filter_header.lower():
                    counter = counter + 1
                    print (f" Juego {counter}   -    {game['Name']}.....(Desarrollador:{game['Developer'].upper()} / Genero: {game['Genre']})")
            print(f"Total de juegos registrados: {counter}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return 0  


def report_file_by_gender(file_path):
    try:
        counter = 0
        genre_count={}
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            sum_list=[]
            for game in reader:
                genre = game ['Genre'].upper()
                if genre in genre_count:
                    genre_count[genre] = genre_count[genre]+1
                else:
                    genre_count[genre] = 1

        
        print("------------------Reporte de juegos por género-----------------------")
        for char, count in genre_count.items():
            print(f"{char}......{count}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return 0


def report_file_by_developer(file_path):
    try:
        counter = 0
        developer_count = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            filter_header = input(f"Ingrese el nombre del desarrollador: ")
            for game in reader:
                if game ['Developer'].lower() == filter_header.lower():
                    counter = counter + 1
                    print (f"...................Juegos desarrollados por {game['Developer']}................")
                    print (f" - Nombre:   {game['Name']}.....(Clasificación:{game['ESRB rating']} / Genero: {game['Genre']})")
            print(f"Total de juegos registrados: {counter}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return 0

def resume_file_by_developer(file_path):
    try:
        counter = 0
        developer_count={}
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            sum_list=[]
            for game in reader:
                developer = game ['Developer'].upper()
                if developer in developer_count:
                    developer_count[developer] = developer_count[developer]+1
                else:
                    developer_count[developer] = 1
        print("------------------Estos son los desarrolladores registrados-----------------------")
        for char, count in developer_count.items():
            print(f"{char}......{count}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return 0

    
def main():
    while True:
        print("-------------------Menú Principal----------------")
        print("1- Mostrar los datos del archivo")
        print("2- Ingresar un nuevo registro")
        print("3- Salir")
        main_menu_option = int(input(f"Ingrese una opción: "))
        ruta_terminal = os.path.dirname(os.path.abspath(__file__))+"/games_input_extra_exc2.csv"
        #print(ruta_terminal)

        if main_menu_option == 1:
            print("---------------Menú de consultas de datos del archivo-------------------")
            print("1- Consulta por ESRB rating")
            print("2- Consulta por Genero")
            print("3- Consulta por Desarrollador")
            print("4- Volver al menú anterior")
            report_menu_option = int(input(f"Ingrese una opción: "))
            if report_menu_option == 3:
                resume_file_by_developer (ruta_terminal)
                report_file_by_developer (ruta_terminal)
            if report_menu_option == 1:
                report_file_by_rating (ruta_terminal)
            if report_menu_option == 2:
                report_file_by_gender (ruta_terminal)
            if report_menu_option == 4:
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
            print("Cerrando el programa.............. Nos vemos pronto!")
            break
main()

# Esta pendiente poder ver la lista de desarrolladores para poder hacer la consulta de una mejor manera.
# Una opcion es hacer otra funcio para solo mostrar un resumen por desarrollador
