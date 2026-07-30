#Este programa muestra las notas de un estudiante y define si el estudiante aprueba o no, dependiendo de su nota final
print("------------Reporte de notas------------")
name = input("Ingrese el nombre del estudiante: ")
Total_note = int(input("Ingrese la cantidad de notas a revisar: "))
Note_counter = 1
Actual_note = 0
approved_note_qty=0
failed_note_qty=0
avg_approved_note=0
avg_failed_note=0
total_avg_note = 0
sum_note = 0 # esta variable es la que me va a permitir calcular el promedio total de notas del estudiante, sumando todas las notas ingresadas por el usuario
while Note_counter <= Total_note:
    print("ingrese la nota", Note_counter, "del estudiante")
    Actual_note = float(input())
    sum_note = sum_note + Actual_note
    if Actual_note < 70:
        failed_note_qty = failed_note_qty + 1
        avg_failed_note=avg_failed_note + Actual_note
    else:
        approved_note_qty = approved_note_qty + 1
        avg_approved_note=avg_approved_note + Actual_note
    Note_counter += 1
total_avg_note = sum_note / Total_note
if failed_note_qty > 0: #voy a cambiar la condición a ">" para que el programa solo calcule el promedio de notas reprobadas si el estudiante tiene al menos una nota reprobada, de lo contrario, el promedio de notas reprobadas se establecerá en 0. Esto es importante para evitar la división por cero al calcular el promedio de notas reprobadas. Si el estudiante no tiene notas reprobadas, no se puede calcular un promedio de notas reprobadas, por lo que se establece en 0.
    avg_failed_note = avg_failed_note / failed_note_qty
else:
    avg_failed_note = 0 #Si el estudiante no tiene notas reprobadas, el promedio de notas reprobadas se establece en 0, para evitar la división por cero al calcular el promedio.
if approved_note_qty > 0: #voy a cambiar la condición a ">" para que el programa solo calcule el promedio de notas aprobadas si el estudiante tiene al menos una nota aprobada, de lo contrario, el promedio de notas aprobadas se establecerá en 0. Esto es importante para evitar la división por cero al calcular el promedio de notas aprobadas. Si el estudiante no tiene notas aprobadas, no se puede calcular un promedio de notas aprobadas, por lo que se establece en 0.
    avg_approved_note = avg_approved_note / approved_note_qty
else:
    avg_approved_note = 0 #Si el estudiante no tiene notas aprobadas, el promedio de notas aprobadas se establece en 0, para evitar la división por cero al calcular el promedio.
total_avg_note = sum_note / Total_note
print("El estudiante", name, ", tiene un total de ", Total_note, " notas, de las cuales", approved_note_qty, " han sido aprobadas, con un promedio de", avg_approved_note, ",y tiene ", failed_note_qty, "notas reprobadas, con un promedio de", avg_failed_note, "y un promedio total de", total_avg_note  )
