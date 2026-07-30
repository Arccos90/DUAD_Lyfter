#Este programa imprime los datos de 2 listas
print("-------Listas de cosas-------")
first_list = ["Hay", "en", "que", "iteración", "indices", "muy"]
second_list = ["casos", "los","la","por","es","util"]
print("Primera lista: ", first_list)
print("Segunda lista: ", second_list)
counter=0
while counter < len(first_list):
    print(first_list[counter],second_list[counter]) #se imprimen los elementos de las listas utilizando el contador como índice para acceder a cada elemento de ambas listas.
    counter+=1    