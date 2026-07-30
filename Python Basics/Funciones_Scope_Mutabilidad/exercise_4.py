"Exercise 4: Funciones, Scope y Mutables"


def reverse_string(my_string):
    inverted_text = ""
    for char in range(len(my_string)-1,-1,-1):
     inverted_text = inverted_text + my_string[char]
    return inverted_text
def main():
    original_text =input("Ingrese una frase:") # El valor de la variable original_text, se usa como el valor para la función reverse_string
    final_text = reverse_string(original_text)
    print(f"Su frase invertida es: {final_text}")

main()
