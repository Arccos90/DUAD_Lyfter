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
    saved_students = []
    try:
        counter = 0
        total_couter = counter_data_on_file (file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            print("""
-------------------------------------------------------
            
            """)
            print(f"!Se importaron {total_couter} estudiantes(s)!")  
            print("""
-------------------------------------------------------
            """)
            for student in reader:
                student_dict = {
                    'ID': int(student['ID']),
                    'student_name': student['student_name'],
                    'last_name': student['last_name'],
                    'second_surname': student['second_surname'],
                    'type': student['type'],
                    'spanish': float(student['spanish']),
                    'english': float(student['english']),
                    'socials': float(student['socials']),
                    'science': float(student['science']),
                    'avg_note': float(student['avg_note'])            
                }
                saved_students.append(student_dict)
        return saved_students
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return saved_students


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


def avg_read_temporary_file (temporary_file):
        counter = 0
        total_counter = len(temporary_file)

        print("""
-------------------------------------------------------
            
            """)
        print(f"!Hay {total_counter} estudiantes(s) ingresado(s)!")  
        print("""
-------------------------------------------------------
            """)
        print("Nombre Completo --------Nota Promedio")
        for student in temporary_file:
                counter = counter + 1
                print(f"{counter}-{student['student_name']} {student['last_name']} {student['second_surname']} --- {student['avg_note']}")
        print("---------final del reporte-----------")
        print("-"*50)
        return counter

    

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


def avg_sort_temporary_file (temporary_file):
        sort_list=[]
        counter=0
        print("--Nombre Completo --------- Nota Promedio")
        for student in temporary_file:
            sort_list.append(student)#hay que crear una lista de los datos de .csv para poder aplicar el método .sort()
                
        sort_list.sort(key=lambda x: float(x['avg_note']), reverse=True) # hay que convertir los datos que viene con string en float
        top_three=sort_list[:3]
        for students in top_three: #se crea un diccionario con el top 3 seleccionado 
            counter=counter+1
            print(f"{counter}-{students['student_name']} {students['last_name']} {students['second_surname']}----{students['avg_note']}")


def avg_total_temporary_file (temporary_file):
    counter = 0
    total_counter = len(temporary_file)   
    print("""
-------------------------------------------------------
            
            """)
    print(f"!Hay {total_counter} estudiantes(s) ingresado(s)!")  
    print("""
-------------------------------------------------------
            """)
    if total_counter > 0:
        total_sum = sum(student['avg_note'] for student in temporary_file)
        counter = counter + 1
        total_counter = len(temporary_file) 
        general_avg = total_sum/total_counter
        print(f"El promedio general es: {general_avg}")
    else:
        print("No hay datos de estudiantes registrados")
        print("---------final del reporte-----------")
        print("-"*50)
        return counter


terminal_route = os.path.dirname(os.path.abspath(__file__))+"/Student_BD.csv"
