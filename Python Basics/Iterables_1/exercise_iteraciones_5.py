print("--------Ejercicio 5 Iteraciones--------")
#Este progrma permite ingresar números y encontrar el número más alto
print("Por favor, ingrese diez números: ")
counter=0
my_list=[] #se declara la lista vacía para almacenar los números ingresados por el usuario
while counter < 10:
    number=float(input(f"Ingrese el número {counter+1}: "))
    my_list.append(number) #se agregan los números conforme sean ingresados por el usuario utilizando el método append.
    counter+=1

print("Lista de números ingresados:", my_list)
print("El número más alto es:", max(my_list)) #max es una función en pyton para obtener el número más alto de una lista.