print("-----------Ejercicio Iterables y Listas #1---------")
counter_numbers = int(input("¿Cuantos números desea ingresar?:"))
my_list = []
find_number = int(input("Que número desea buscar:"))
counter = 0
numbers = 0
while counter < counter_numbers:
        counter = counter + 1
        numbers = int(input("Por favor ingrese un número " + str(counter) + ": ")) #
        my_list.append(numbers)
print("números ingresados:", my_list)

find_numbers_result= my_list.count(find_number)
#El método count() devuelve el número de veces que un elemento aparece en la lista, por lo que se utiliza para contar cuantas veces se encuentra el número que se busca en la lista.
if find_numbers_result > 1: 
    #Esta linea es para verificar si aparec mas de 1 vez y que el texto coincida con la cantidad de veces. 
    print("El número", find_number, "aparece", find_numbers_result, "veces en la lista.")
elif find_numbers_result == 1:
    print("El número", find_number, "aparece", find_numbers_result, "vez en la lista.")
else:
    print("El número", find_number, "no se encuentra en la lista.")