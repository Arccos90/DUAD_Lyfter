"Ejercicio Extra #1: Iterables y listas"
total_counter = int (input ("Indique cuantos números desea ingresar:"))
counter = 0
target_number = int (input("Indique que número desea buscar:"))
my_list = []
target_counter = 0
while counter < total_counter:
    number =  int(input(f"ingrese el número {counter+1}: "))
    my_list.append (number)
    counter+=1
print (my_list)
target_list = []
for char in my_list:
    if char == target_number:
        target_counter = target_counter + 1
        target_list.append(char)
total_target_number = len(target_list)
print (f"El número objetivo es {target_number}, se ha encontrado {total_target_number} veces")
print (f" La forma recomendada es hacerlo así: El {target_number}, aparece {target_counter} veces.")