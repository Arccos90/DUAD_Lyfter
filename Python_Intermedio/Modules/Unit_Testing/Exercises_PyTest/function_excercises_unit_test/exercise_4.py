"Exercise 4: Funciones, Scope y Mutables"

<<<<<<< HEAD
def reverse_string(my_string):
    if "$" in my_string:
        raise ValueError("El texto no debe contener el símbolo $")
=======

def reverse_string(my_string):
>>>>>>> ce849ab48ae1d3dfe7f855aefc5fc4c5d23b4fda
    inverted_text = ""
    for char in range(len(my_string)-1,-1,-1):
     inverted_text = inverted_text + my_string[char]
    return inverted_text
def main():
    original_text =input("Ingrese una frase:") # El valor de la variable original_text, se usa como el valor para la función reverse_string
    final_text = reverse_string(original_text)
    print(f"Su frase invertida es: {final_text}")

<<<<<<< HEAD
if __name__== "__main__":
    main()
=======
main()
>>>>>>> ce849ab48ae1d3dfe7f855aefc5fc4c5d23b4fda
