print("-------------------------Extra_Exercise_#2-----------------------------------")

def main ():
    #Esta es la funcion principal que permite operar el programa
    word_list=[]
    while True:
        print ("--------------------Menú principal------------------------")
        print (f"Palabras ingresadas: {len(word_list)}")
        print ("(1) - Ingresar una palabra.")
        print ("(2) - Ver palabras ingresadas.")
        print ("(3) - Clasificar palabras por número de letras.")
        print ("(4) - Borrar todo.")
        print ("(5) - Salir.")
        try:
            menu_option = int(input(f"Elija que opcion desea realizar: "))
        except ValueError:
            print (f"Ingrese una opción valida")
            continue
        if menu_option == 1:
            word_list= input_words(word_list)
            print(f"Lista de palabras: {word_list}")
        elif menu_option == 2:
             visual_words(word_list)
        elif menu_option == 3:
             classification_words(word_list)
        elif menu_option == 4:
             clean(word_list)
        elif menu_option == 5:
              print ("Cerrando el programa. !Nos vemos pronto!")
              break



def input_words (current_list):
    
        print ("Ingrese palabras una por una, escriba la palabra <salir> para terminar.")
        while True: 
            words = str(input(f"Ingrese una palabra:")).strip() 
            if words.lower() == 'salir':
                 break
            if words:
                current_list.append(words)
                print(f"{current_list}")
            word_counter = len(current_list) #quiero contar las palabras ingresadas para que se vean en el menu inicial
        return current_list


def visual_words(current_list):
     
     if len(current_list) == 0:
          print("La lista está vacía. Ingresa una palabra")
          return
     
     print("\n------------------Lista de palabras ingresadas----------------------- ")
     for numero, palabra in enumerate(current_list, start=1):
        print(f"{numero}. {palabra}")


def classification_words(current_list):
     
    if len(current_list) == 0:
          print("La lista está vacía. Ingresa una palabra")
          return
    try:
        counter_char_parameter = int(input(f"Ingrese la cantidad de letras por palabra: "))
    except ValueError:
         return
     
    temporaly_list = []
    for char in current_list:
          counter_char = len(char)
          if len(char) >= counter_char_parameter:
            temporaly_list.append(char)


    print(f"\n------- Las palabras con más de {counter_char_parameter} letras son:  ------------------")

    if len(temporaly_list) == 0:   
        print("No se encontraron palabr_as con esa cantidad de letras.")
    else: 
        for numero, palabra in enumerate(temporaly_list, start=1):
                print (f"{numero}. {palabra}")

def clean (current_list):
    current_list.clear()
    print("Los datos se borraron correctamente")
    return current_list


word_counter = 0



main()
