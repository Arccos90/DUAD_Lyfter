print("--------------------Extra_Exercise_#1----------------------------------")

def input_text (my_string, char):
    counter = 0
    target = char
    for char_f in my_string:
        if char_f == target:
            counter = counter+1
    print(f"El caracter {target}, sale {counter} veces en el texto")

def main():
    text = str(input(f"Ingrese un texto: "))
    character = str(input(f"Ingrese el caracter que desea buscar: "))
    input_text(text,character)

main()