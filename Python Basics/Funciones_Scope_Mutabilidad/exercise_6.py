"Exercise 6: Funciones, Scope y Mutables"


def alphabetical_order (my_string):
     jumbled_words_list = my_string.split("-")
     jumbled_words_list.sort()
     order_word_text = "-".join(jumbled_words_list)
     return order_word_text

    
def main():
    original_text =input("Ingrese una frase:")
    modify_text = original_text.replace(" ","-")
    final_text_order = alphabetical_order(modify_text)
    
    print(f"The original text was: {modify_text}, and the final text is: {final_text_order}")

main()