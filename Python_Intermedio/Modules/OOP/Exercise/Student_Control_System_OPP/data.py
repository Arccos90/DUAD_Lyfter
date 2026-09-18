"---------------------------Data Management----------------------------"
import csv
import os
from Student import Student

terminal_route = os.path.dirname(os.path.abspath(__file__)) + "/Student_BD.csv"

def write_on_file(file_path, student_list):
    if not student_list:
        print("No hay estudiantes para guardar.")
        return
    # Convertimos cada objeto a diccionario para DictWriter
    dict_data = [student.to_dict() for student in student_list]
    headers = dict_data[0].keys()
    with open(file_path, 'w', encoding='utf-8', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(dict_data)
    print("¡Datos exportados con éxito!")

def append_on_file(file_path, student_list):
    if not student_list:
        return
    dict_data = [student.to_dict() for student in student_list]
    headers = dict_data[0].keys()
    with open(file_path, 'a', encoding='utf-8', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t")
        writer.writerows(dict_data)

def read_file(file_path):
    saved_students = []
    try:
        total_counter = counter_data_on_file(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            print("\n-------------------------------------------------------")
            print(f"!Se importaron {total_counter} estudiante(s)!")
            print("-------------------------------------------------------\n")
            for row in reader:
                # Cada fila se transforma en una instancia de Student
                saved_students.append(Student.from_csv_row(row))
        return saved_students
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return saved_students

def counter_data_on_file(file_path):
    try:
        counter = 0
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter="\t")
            for _ in reader:
                counter += 1
        return counter
    except FileNotFoundError:
        return 0

def avg_read_temporary_file(temporary_file):
    total_counter = len(temporary_file)
    print("\n-------------------------------------------------------")
    print(f"!Hay {total_counter} estudiante(s) ingresado(s)!")
    print("-------------------------------------------------------\n")
    print("Nombre Completo -------- Nota Promedio")
    for counter, student in enumerate(temporary_file, start=1):
        # Acceso por atributos de objeto:
        print(f"{counter}- {student.student_name} {student.last_name} {student.second_surname} --- {student.avg_note:.2f}")
    print("---------final del reporte-----------")
    print("-" * 50)
    return total_counter

def avg_sort_temporary_file(temporary_file):
    if not temporary_file:
        print("No hay datos para mostrar.")
        return
    # Ordenamos directamente por el atributo avg_note
    sorted_list = sorted(temporary_file, key=lambda student: student.avg_note, reverse=True)
    top_three = sorted_list[:3]

    print("\n--Nombre Completo --------- Nota Promedio")
    for counter, student in enumerate(top_three, start=1):
        print(f"{counter}- {student.student_name} {student.last_name} {student.second_surname} ---- {student.avg_note:.2f}")

def avg_total_temporary_file(temporary_file):
    total_counter = len(temporary_file)
    print("\n-------------------------------------------------------")
    print(f"!Hay {total_counter} estudiante(s) ingresado(s)!")
    print("-------------------------------------------------------\n")
    if total_counter > 0:
        total_sum = sum(student.avg_note for student in temporary_file)
        general_avg = total_sum / total_counter
        print(f"El promedio general es: {general_avg:.2f}")
    else:
        print("No hay datos de estudiantes registrados")
    print("---------final del reporte-----------")
    print("-" * 50)