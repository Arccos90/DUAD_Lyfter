print("-----------Ejercicio Iteralbles + listas #2---------")

counter_numbers = int(input("¿Cuantos números desea ingresar?:"))
my_list = []
counter = 0
numbers = 0
negative_list =[]
while counter < counter_numbers:
        counter = counter + 1
        numbers = int(input("Por favor ingrese un número " + str(counter) + " (puede ser negativo o cero): ")) #
        my_list.append(numbers)
print("números ingresados:", my_list)
for negative_number in my_list :
        if negative_number <= 0:
            negative_list.append(negative_number)
            #print(negative_list)
        negative_counter = len(negative_list)
if negative_counter == 1:
       print ("Hay ",negative_counter," número negativo o igual a cero")
elif  negative_counter > 1:
    print ("Hay ",negative_counter," números negativos o iguales a cero")
elif negative_counter == 0:
    print ("No hay números negativos o ceros")