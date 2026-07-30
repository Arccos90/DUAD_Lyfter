"Ejercicio Extra #3: Iterables y listas"
#Cree un programa que verifique si todos los elementos de una lista son positivos
counter_number = int (input ("¿Cuantas palabras desea ingresar:? "))
my_list = []
counter = 0
total_word = 0 #Recomendación para evitar error por palabras con menos de 4 letras.
while counter < counter_number:
    string = (input(f"Ingrese la palabra {counter+1}: "))
    my_list.append(string)
    counter+=1

comparable_list= []
for char in my_list:
    if len(char) > 4:
        comparable_list.append(char)
        total_word=len(comparable_list)

print (f"Hay un total de {total_word} palabras con mas de 4 letras, la palabras son: {comparable_list}")
