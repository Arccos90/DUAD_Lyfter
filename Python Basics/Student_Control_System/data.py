"---------------------------Data Management----------------------------"
import csv
import os
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
        total_couter = counter_data_on_file (terminal_route)
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            print("""
-------------------------------------------------------
            
            """)
            print(f"!Hay {total_couter} estudiantes(s) ingresado(s)!")  
            print("""
-------------------------------------------------------
            """)
            for student in reader:
                counter = counter + 1
                print(f"Estudiante {counter}")
                print(f"  - Nombre Completo: {student['student_name']} {student['last_name']} {student['second_surname']}")
                print(f"  - Id:              {student['ID']}")
                print(f"  - Sección:         {student['type']}")
                print("------------Notas-------------")
                print(f"  - Español:       {student['spanish']}")
                print(f"  - Inglés:        {student['english']}")
                print(f"  - Sociales:      {student['socials']}")
                print(f"  - Ciencias:      {student['science']}")
                print(f"  ------ Promedio:-----{student['avg_note']}---")
                print("-"*50)
            print("final del reporte")
            print("-"*50)
        return counter
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return 0 # Si no existe el archivo brinca hasta el except y no retorna ningún valor, por lo que genera un error en la formula main()


def counter_data_on_file(file_path):
    try:
        counter = 0
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            for student in reader:
                counter = counter + 1

        return counter
    except FileNotFoundError:
        return 0


def avg_read_file (file_path):
    try:
        counter = 0
        total_couter = counter_data_on_file (terminal_route)
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            print("""
-------------------------------------------------------
            
            """)
            print(f"!Hay {total_couter} estudiantes(s) ingresado(s)!")  
            print("""
-------------------------------------------------------
            """)
            print("Nombre Completo --------Nota Promedio")
            for student in reader:
                counter = counter + 1
                print(f"{counter}-{student['student_name']} {student['last_name']} {student['second_surname']} --- {student['avg_note']}")
            print("---------final del reporte-----------")
            print("-"*50)
        return counter
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return 0 # Si no existe el archivo brinca hasta el except y no retorna ningún valor, por lo que genera un error en la formula main()
 

def avg_sort_read_file (file_path):
    try:
        sort_list=[]
        sort_top={}
        counter=0
        print("--Nombre Completo --------- Nota Promedio")
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            for student in reader:
                sort_list.append(student)#hay que crear una lista de los datos de .csv para poder aplicar el método .sort()
                
        sort_list.sort(key=lambda x: float(x['avg_note']), reverse=True) # hay que convertir los datos que viene con string en float
        top_three=sort_list[:3]
        for students in top_three: #se crea un diccionario con el top 3 seleccionado 
            counter=counter+1
            print(f"{counter}-{students['student_name']} {students['last_name']} {students['second_surname']}----{students['avg_note']}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return 0


terminal_route = os.path.dirname(os.path.abspath(__file__))+"/Student_BD.csv"
