import os
print("--------------------------Exercise_#3: Files Management--------------------------------")


def read_files_by_lines (path):
    try:    
        with open(path, 'r', encoding='utf-8') as file:
            word_list= []
            new_word_list = []
            counter = 0
            for line in file.readlines(): #inicialmente usé .strip() para eliminar '\n', pero al final en la formula para copiar en el archivo me sale todo en una sola linea, pero si no lo quito la formula los detecta como saltos de linea
                word_list.append(line)
        
            print (f"Esta es la información del archivo:")
            print (f"{"".join(word_list)}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {path}")
    return word_list


def words_counter(my_list): #Esta funcion es una manera alternativa de contar las palabras del archivo desde otra funcion
    counter = 0
    for char in my_list:
        counter = counter + 1
    print(f"Este es el contador 2: El archivo tiene {counter} palabras")


def upper_converter (my_list):
        new_my_list = []
        for char in my_list:
            upper_char = char.upper()
            new_my_list.append(upper_char)
        print(f"Esta es la informacion del nuevo archivo: ")
        print (f"{"".join(new_my_list)}")
        return new_my_list

def write_new_file_by_lines (path,my_list):
    with open (path,'w', encoding='utf-8') as file:
        file.writelines(my_list)



def main():    
    ruta_terminal = os.path.dirname(os.path.abspath(__file__))+"/Text_input_exc3.txt" # de esta manera me aseguro de usar la ruta absoluta. No me esta funcionando el uso de rutas relativas.
    #print(ruta_terminal)
    ruta_terminal_new_file = os.path.dirname(os.path.abspath(__file__))+"/Text_input2_exc3.txt"
    
    new_list = read_files_by_lines (ruta_terminal) 
    print ("---------------------------- Resultado--------------------------------------")  
    new_list_converted = upper_converter (new_list)
    write_new_file_by_lines (ruta_terminal_new_file,new_list_converted)
    print (f"Los datos se copiaron correctamente en el archivo: {ruta_terminal_new_file}")
main()