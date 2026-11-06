"--------exercise 3: Funciones, Scope y Mutables--------"

def sum_numbers(number_list):
    total = 0
    for number in number_list:
        total += number
    print("La suma de los números en la lista es:", total)
    return total

def main():
    number_list = [12, 45, 67, 89, 23, 56, 78]
    sum_numbers(number_list)

if __name__== "__main__":
    main()