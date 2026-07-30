"Ejercicio Extra #3: Iterables y listas"
#Cree un programa que verifique si todos los elementos de una lista son positivos
counter_number = int (input ("¿Cuantos números desea ingresar? "))
my_list = []
counter = 0
while counter < counter_number:
    number = int (input(f"Ingrese el número {counter+1}: "))
    my_list.append(number)
    counter+=1
average = sum (my_list)/counter
comparable_list= []
for char in my_list:
    if char > average:
        comparable_list.append(char)

print (f"El promedio es igual a: {average}, los número mayores al promedio son: {comparable_list}")
