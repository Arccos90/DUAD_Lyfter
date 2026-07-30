print("-------------------------Extra_Exercise_#3-----------------------------------")
print (".................Contador de vocales en una frase...........................")

def main ():
    #Esta es la funcion principal que permite operar el programa
    word_list=[]
    while True:
        print ("--------------------Menú principal------------------------")
        print (f"Frases ingresadas: {len(word_list)}")
        print ("(1) - Ingresar una frase.")
        print ("(2) - Ver la frase ingresada.")
        print ("(3) - Contar las vocales en la frase.")
        print ("(4) - Borrar todo.")
        print ("(5) - Salir.")
        try:
            menu_option = int(input(f"Elija que opcion desea realizar: "))
        except ValueError:
            print (f"Ingrese una opción valida")
            continue
        if menu_option == 1:
            word_list= input_phrase(word_list)
            print(f"Lista de palabras: {word_list}")
        elif menu_option == 2:
             visual_phrase(word_list)
        elif menu_option == 3:
             vowel_counter(word_list)
        elif menu_option == 4:
             clean(word_list)
        elif menu_option == 5:
              print ("Cerrando el programa. !Nos vemos pronto!")
              break



def input_phrase (current_list):
    
        print ("Ingrese la frase que desea analizar con el programa:")
       
        words = str(input(f"Frase  :"))
        current_list.append(words)
        print(f"{current_list}")
        word_counter = len(current_list) #quiero contar las palabras ingresadas para que se vean en el menu inicial
        return current_list


def visual_phrase(current_list):
     
     if len(current_list) == 0:
          print("La lista está vacía. Ingresa una frase")
          return
     
     print("\n------------------La frase ingresada es: ---------------------- ")
     for numero, palabra in enumerate(current_list, start=1):
        print(f"{numero}. {palabra}")


def vowel_counter(current_list):
     
    if len(current_list) == 0:
          print("La lista está vacía. Ingresa una frase")
          return
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    vowels_counter = 0
    temporaly_list = []
    for word in current_list:
        for char in word:
          if char in vowels:
            temporaly_list.append(char)
            vowels_counter = len(temporaly_list)
    print(f"La frase tiene {vowels_counter} vocales")
    return(temporaly_list)

def clean (current_list):
    current_list.clear()
    print("Los datos se borraron correctamente")
    return current_list


word_counter = 0



main()