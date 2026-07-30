"Ejercicio Extra #2: Iterables y listas"
#Cree un programa que verifique si todos los elementos de una lista son positivos
counter_number = int (input ("¿Cuantos números desea ingresar? "))
my_list = []
counter = 0
while counter < counter_number:
    number = int (input(f"Ingrese el número {counter+1}: "))
    my_list.append(number)
    counter+=1
negative_list=[]   
for char in my_list:
    if char <= 0: #agregada la sugerencia
        negative_list.append(char)

total_negative = len(negative_list)
       
if total_negative == 0:
     print(f"Todos los {counter_number} números de la lista son positivos")
else:
     print(f"No todos los números son positivos, hay {total_negative} negativos")