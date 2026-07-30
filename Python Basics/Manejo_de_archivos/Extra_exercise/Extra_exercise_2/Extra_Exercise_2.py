
import os
print("--------------------------Exercise_#2: Files Management--------------------------------")


def read_files_by_lines (path):
    with open(path, 'r', encoding='utf-8') as file:
        word_list= []
        counter = 0
        lines = file.read().replace("\n"," ")
        print (f"Este es el contenido del archivo: {lines}")
        word_list = lines.split()
        #print(word_list)
        counter = len (word_list)
        print (f"Este es el contador 1: Hay {counter} palabras en el archivo")
    return word_list


def words_counter(my_list): #Esta funcion es una manera alternativa de contar las palabras del archivo desde otra funcion
    counter = 0
    for char in my_list:
        counter = counter + 1
    print(f"Este es el contador 2: El archivo tiene {counter} palabras")


def main():    
    ruta_terminal = os.path.dirname(os.path.abspath(__file__))+"/Text_input_exc2.txt" # de esta manera me aseguro de usar la ruta absoluta. No me esta funcionando el uso de rutas relativas.
    #print(ruta_terminal)

    print ("---------------------------- Resultado--------------------------------------")
    new_list = read_files_by_lines (ruta_terminal)
    #print(f"Esta es la nueva lista: {new_list}")
    words_counter (new_list)
  
main()