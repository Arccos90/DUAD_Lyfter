print("------------------Exercise_#3----------------------")

def input_to_list ():
    my_list = []
    counter =0
    My_string = 0
    while True:
        
        My_string = input(f"Ingrese un número a la lista o <salir> para terminar: ")
        
        if My_string != "salir":
            my_list.append(My_string)
            counter = len(my_list)
            print("Los datos ingresados son:")
            print(f"{my_list}")
            continue
        elif My_string == "salir" and len(my_list) == 0:
            print("Lista vacía")
            break
        elif My_string == "salir":
            print(f"{my_list}")
            break
        
    return my_list

def convert_to_list (list_input):
    list_to_convert=list_input
    list_sum = []
    print(f"Verificador: Esta es la lista para modificar {list_to_convert}") #Este print me permite saber si estoy obteniendo los datos correctos de la formula input_to_list
    print("------Resultado-----")
    for item in list_to_convert:
        try:
            int_item = float(item)
            print(f"{item} convertido a {int_item}")
            list_sum.append(int_item)
        except IndexError as error:
            print(f"El indice a usar no existe en la lista. Error {error}")
        except ValueError as error:
            print(f"No se pudo convertir el elemento {item}. El elemento de la lista no es un número válido. Error {error}")
    return list_sum
def value_sum(my_sum_list):
    finaly_sum = sum (my_sum_list)
    print(f"Total de la suma: {finaly_sum}")

def main():
    
    while True:
        new_my_list = input_to_list()
        new_list_sum = convert_to_list(new_my_list)
        
        if len(new_my_list)== 0:
            continue
        elif len(new_my_list) > 0:

            print(f"Verificador: Estos son los datos ingresados:  {new_my_list}") #Valida que estoy trayendo la lista de las formulas.
            print(f"Verificador: Lista de valores sumable: {new_list_sum}")
            value_sum(new_list_sum)
            break

main()