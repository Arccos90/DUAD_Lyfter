print("--------Ejercicio 3 Diccionarios--------")
list_of_keys = ["access_level", "age"]
employee = {
    "name": "John", 
    "email": "john@ecorp.com", 
    "access_level": 5,
    "age": 28,
    }
print("Employee before deletion:", employee)
counter = 0
number_of_keys = len(list_of_keys)
print("Number of items to delete:", number_of_keys)
if number_of_keys > counter:  
    while counter < number_of_keys:
        deleted_key = employee.pop(list_of_keys[counter]) 
        print(f"deleted items # {counter+1}: {deleted_key}")
        counter += 1
print("Employee after deletion:", employee) 
#se imprime el diccionario después de eliminar las claves especificadas en la lista, mostrando el resultado final.   



print("----Metodo alternativo o simplificado----")
#el metodo anterior podría dar error si la clave a eliminar no existe en el diccionario, por lo que se puede utilizar el método pop() con un valor predeterminado para evitar errores.
list_of_key_2 = ["access_level", "age"]
employee_2 = {
    "name": "John", 
    "email": "john@ecorp.com", 
    "access_level": 5,
    "age": 28,
    }

for key_2 in list_of_key_2:
    deleted_key = employee_2.pop(key_2, None) 
    #None se utiliza como valor predeterminado para evitar errores si la clave no existe en el diccionario.
    print(f"deleted item : {deleted_key}")
print("Employee after deletion:", employee_2)   