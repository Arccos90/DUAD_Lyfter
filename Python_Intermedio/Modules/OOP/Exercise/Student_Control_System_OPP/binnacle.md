# Binnacle of project: Student_Control_System

## 📅 Session: Friday (07/08/26)
** Status: 
** Module 'main' works well, i worked on the option 1 capabilities. Already call the function of the module 'data' and 'actions'. Beside the program can save the data on the .csv file. 
_Also, i worked on the menu option 2. It brings the report with all students inside the .csv file. 
_Also, I did the report for the menu option 4, it brings a report by student.

** Module 'menu'have all the options to manage the program and I made a AIIC design with the program's name and the version.


-** Blocks or doubts: **
-**📌 To do: ** 
[] to work on the option 3. Try to get the top 3 data of the avg notes and sort. I think that, maybe could be a good idea to make a new call from the .csv file and sort the data from the avg note, and then, make a function that show me the first 3 data.
[] to work on the option 5. Works on a report with a student filter. I think that, i could make a extra menu on this part, and bring the option to choice while kind of data the user would choice. For example, filter by name or second name or other filter by section.

## 📅 Session: Monday (10/08/26)
** Agenda:
[X] to work on the option 3. Try to get the top 3 data of the avg notes and sort. I think that, maybe could be a good idea to make a new call from the .csv file and sort the data from the avg note, and then, make a function that show me the first 3 data.
** STATUS
    _I did the function 'avg_sort_read_file', this function read the .csv file and then it sort the data by avg_note and then filter the first three students. I used the method .sort() and found extra features that give me the possibility to order the list without fails results like 'none'and allows float result.
                    sort_list.sort(key=lambda x: float(x['avg_note']), reverse=True)

**📌 To do: **                    
[] to work on the option 5. Works on a report with a student filter. I think that, i could make a extra menu on this part, and bring the option to choice while kind of data the user would choice. For example, filter by name or second name or other filter by section.
[] Create option 7. Find a student by name and section. Aks to confirm before to delete.

** Blocks or doubts: **
    _ I am not sure about how find data with 2 criteria. I am thinking to use a extra key. Like name + section. I should to search something about that.
    _ Maybe I will should to combine the option 5 and 7. I think that they makes the same function.


## 📅 Session: Tuesday (26/08/26)
** Agenda:
[] 1. Lista en memoria vs. CSV
    Debe trabajar primero con una lista en memoria, y que el CSV se usa únicamente cuando el usuario elige exportar o importar. Actualmente, los datos se guardan directo al CSV al ingresar un estudiante, y los reportes leen desde el archivo. Lo que se espera es: mantener una lista de diccionarios activa durante la sesión, y solo escribir/leer el CSV cuando el usuario lo pida explícitamente desde el menú.
[] 2. Opciones de Exportar e Importar en el menú
    Faltan dos opciones dedicadas en el menú: una para exportar los datos actuales al CSV, y otra para importar desde un CSV existente. La importación debe cargar los datos en la lista en memoria del programa. Si no existe el archivo al importar, debe informárselo al usuario sin que el programa se rompa.
[] 3. Promedio general entre todos los estudiantes
    Esta es una de las funciones requeridas y aún no está implementada. Debe calcular el promedio de los promedios de todos los estudiantes y mostrarlo al usuario desde una opción del menú.
[] 4. Bug en data.py: variable no definida dentro de funciones
    Las funciones read_file() y avg_read_file() usan terminal_route internamente, pero esa variable no está definida dentro de su scope, solo existe al final del módulo. Esto causará un NameError al ejecutarlas. Cada función debe recibir la ruta como parámetro (ya lo hace file_path, pero la línea counter_data_on_file(terminal_route) usa la variable global). Además, al final de data.py hay una llamada directa a avg_sort_read_file(terminal_route) que se ejecuta cada vez que el módulo es importado; esa línea debe eliminarse.
[] 5. Validación de entrada en el menú
    La línea int(input(...)) en main.py no está protegida con try/except. Si el usuario escribe texto en vez de un número, el programa se romperá con un ValueError. Lo mismo aplica para float(input(...)) en las notas. Envolver esas conversiones en un bloque try/except permitiría mostrar un mensaje amigable y seguir ejecutando.

**📌 To do: **                    
[] to work on the option 5. Works on a report with a student filter. I think that, i could make a extra menu on this part, and bring the option to choice while kind of data the user would choice. For example, filter by name or second name or other filter by section.
[] Create option 7. Find a student by name and section. Aks to confirm before to delete.