#---------------Example of Bubble Sort--------------------
def bubble_sort(list_to_sort):
    for outer_index in range(0,len(list_to_sort)-1):
        changes_detector = False
        print("-------------------------------------------------------------")
        print(f"Cantidad de interaciones: {len(list_to_sort)-outer_index-1}")
        for index in range(0, len(list_to_sort)-1-outer_index):
            current_element=list_to_sort[index]
            next_element = list_to_sort[index + 1]
            print(f"-- Iteración {outer_index}/{index}: Elemento actual: {current_element}, siguiente elemento: {next_element}")

            if current_element > next_element:
                print("El elemento actual es mayor al siguiente elemento, se intercambiaran")
                list_to_sort[index]=next_element
                list_to_sort[index+1]=current_element
                changes_detector=True
            else:
                print("El elemento actual es menor, no se hará cambios.... continuar con otro elemento")
        if not changes_detector:
            return

my_list = [18,-11,-50,80,5,3,90,-40]
print(f"Lista sin ordenar: {my_list}")
bubble_sort(my_list)
print(f"Esta es la lista ordenada: {my_list}")