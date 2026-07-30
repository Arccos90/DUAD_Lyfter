print ("------------------------Exercise_1: Pokemon_BD_on_JSON---------------------------------")
"1- Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de Manejo de JSON."
"2- Debe leer el archivo para importar los Pokémones existentes."
"3- Luego debe pedir la información del Pokémon a agregar."
"4- Finalmente debe guardar el nuevo Pokémon en el archivo."

import json
import os

def read_json_file (file_path):
    try:
        counter=0
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = json.load (file)
            for pokemon in reader:
                counter = counter+1
                print(f"-------  Pokemon {counter}  ----------")
                print (f"_ Name      --------- {pokemon['name']}")
                print (f"_ Type      --------- {pokemon['type']}")
                print (f"_ Level     --------- {pokemon['level']}")
                print (f"_ Weight    --------- {pokemon['weight_kg']} kg")
                print (f"_ Is_shiny  --------- {pokemon['is_shiny']}")
                print (f"_ Held_item --------- {pokemon['held_item']}")
                print (f"_ Skills    --------- {pokemon['skills']}")
                print (f"_ Stats     --------- {pokemon['stats']}")
                print("_________________________________________________________________________________________")
            return reader
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        return 0


def append_on_json_file (file_path, new_pokemon_data):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            pokemon_list= json.load (file)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}") 
        pokemon_list=[]
    pokemon_list.append(new_pokemon_data)
    with open (file_path, 'w',encoding='utf-8') as file:
        json.dump (pokemon_list,file, indent=4)

def input_new_data ():
    new_pokemon = {}
    new_skill =[]
    new_stats = {}

    print("----------------Please enter the information for the new pokemon-------------------")
    name = str(input(f"Please enter the pokemon's name: "))
    pokemon_type = str(input(f"Please enter the pokemon's pokemon_type: "))
    level = int(input(f"Please enter the pokemon's level: "))
    weight_kg = float(input(f"Please enter the pokemon's weight (kg): "))
    is_shiny = input(f"Is it a pokemon shiny? (s/n): ") .upper ()
    if is_shiny == "N":
        is_shiny = False
    else:
        is_shiny = True
            # hay que hacer una validacion para que devuelva el boliano
    held_item = str(input(f"Please enter the pokemon's held item: "))
    while True:
        input_skill= input(f"Please enter pokemon's skill or write <exit> to finish: ")
        if input_skill.lower() != 'exit':
            new_skill.append(input_skill)
        if input_skill.lower() == 'exit':
            break
    print("Please enter pokemon's stats:")
    new_stats['hp'] = int(input(f"Enter hp stats:"))
    new_stats['attack'] = int(input(f"Enter attack stats:"))
    new_stats['defense'] = int(input(f"Enter defense stats:"))
    new_stats['sp_attack'] = int(input(f"Enter sp attack stats:"))
    new_stats['sp_defense'] = int(input(f"Enter sp defense stats:"))
    new_stats['speed'] = int(input(f"Enter speed stats:"))
# Queda pendiente empaquetar todo los header para el diccionario new_pokemon, tambien hacer la relacion con JSON
    new_pokemon = {
        'name': name,
        'type': pokemon_type,
        'level':level,
        'weight_kg': weight_kg,
        'is_shiny': is_shiny,
        'held_item': held_item,
        'skills' : new_skill,
        'stats': new_stats
    }
    return new_pokemon

def main():
    terminal_route = os.path.dirname(os.path.abspath(__file__))+"/Pokemon_BD.json"
    print(terminal_route)
    read_json_file(terminal_route)
    new_pokemon_info = input_new_data()
    append_on_json_file (terminal_route, new_pokemon_info)



main()