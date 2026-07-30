print("--------Ejercicio 2 Diccionarios--------")
list_a = ["first_name", "last_name", "role"]
list_b = ["Alek","Castillo","sogware engineer"]
counter = 0
dictionary = {}
while counter < len(list_a):
    print(list_a[counter],":",list_b[counter]) 
    #se imprimen los elementos de las listas utilizando el contador como índice para acceder a cada elemento de ambas listas.
    counter += 1
    dictionary[list_a[counter-1]] = list_b[counter-1]
print(dictionary)