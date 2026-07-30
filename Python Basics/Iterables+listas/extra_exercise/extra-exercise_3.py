"Ejercicio Extra #3: Iterables y listas"
#Cree un programa que verifique si todos los elementos de una lista son positivos
counter_number = int (input ("¿Cuantos números desea ingresar? "))
my_list = []
counter = 0
while counter < counter_number:
    number = int (input(f"Ingrese el número {counter+1}: "))
    my_list.append(number)
    counter+=1
actual_minor = my_list [0]
comparable_list= my_list[1:]
for char in comparable_list:
    if char < actual_minor:
        actual_minor = char
print (f"El número menor es: {actual_minor}")

