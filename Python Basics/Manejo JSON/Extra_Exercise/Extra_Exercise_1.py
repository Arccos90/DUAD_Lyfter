print ("------------------------Extra_Exercise_1: Pokemon_BD_on_JSON---------------------------------")
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
        print(f"Error: Doesn't found the file on: {file_path}") 
        return 0


def report_by_type (file_path):
    try:
        counter=0
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = json.load (file)
            type_filter = input(f"Which type do you like to see? :")
            report_in_progress = """

>>>>>> Report in progress >>>>>>
____________________________________________________________
            """
            print(report_in_progress)
            print(f"You have this {type_filter.upper()} pokemon:")
            for pokemon in reader:
                if pokemon['type'].lower()== type_filter.lower():
                    counter = counter+1
                    print (f"_ Pokemon {counter}--------- {pokemon['name'].upper()}")
            
            print("_________________________________________________________________________________________")
            return reader
    except FileNotFoundError:
        print(f"Error: Doesn't found the file on: {file_path}") 
        return 0


def report_by_stats (file_path):
    try:
        counter=0
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = json.load (file) 
            report_in_progress = """

>>>>>> Report in progress >>>>>>
____________________________________________________________
            """
            counter_total=len (reader)
            print(report_in_progress)
            print(f"Pokemon catches: {counter_total}")
            for pokemon in reader:
                counter = counter+1
                print(f"-------  Pokemon {counter} : {pokemon['name']} ----------")
                stat_list = pokemon.get('stats')
                print(f"      Speed----------{stat_list["speed"]}")
                print(f"      Defense--------{stat_list["defense"]}")
                print(f"      Attack---------{stat_list["attack"]}")
                
            print("_________________________________________________________________________________________")
            return reader
    except FileNotFoundError:
        print(f"Error: Doesn't found the file on: {file_path}") 
        return 0


def report_by_avg_level (file_path):
    try:
        counter=0
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = json.load (file) 
            counter_total=len (reader)
            
            report_in_progress = """
            
>>>>>> Report in progress >>>>>>
____________________________________________________________
            """
            print(report_in_progress)
            counter_type = {}
            print(f"Pokemon catches: {counter_total}")
            for pokemon in reader:
                type_item = pokemon['type']
                level_item = pokemon ['level']
                
                if type_item not in counter_type:
                    counter_type[type_item] = []
                counter_type[type_item].append(level_item)
                
            sum_level ={}
            avg_level ={}
            counter_level={}
            for type_item, level_item in counter_type.items():
                total=sum(level_item) 
                counter= len(level_item)
                avg_level[type_item] = (total/counter)
                counter_level[type_item] = counter
                sum_level[type_item] = total
            print(f"Total of Type: {len(sum_level)}")
            print("__________________________________________")
            for type,level in avg_level.items():
                quantity = counter_level[type]
                suma = sum_level [type]
                
                print (f"""Type: {type}: 
                sum = {suma} | qty = {quantity} | Level average = {level}""")
                
            print("_________________________________________________________________________________________")
            return reader
    except FileNotFoundError:
        print(f"Error: Doesn't found the file on: {file_path}") 
        return 0

def append_on_json_file (file_path, new_pokemon_data):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            pokemon_list= json.load (file)
    except FileNotFoundError:
        print(f"Error: Doesn't found the file on: {file_path}") 
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
    while True:
        terminal_route = os.path.dirname(os.path.abspath(__file__))+"/Pokemon_BD.json"
        logo = """
                ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ██╗ ██████╗ 
                ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔═══██╗
                ██████╔╝██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██║   ██║
                ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██║   ██║
                ██║     ╚██████╔╝██║  ██╗███████╗██║ ╚████║╚██████╔╝
                ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                
                ╔══════════════════════════════════════════════════╗
                ║                 POKEMON WALLET                   ║
                ╚══════════════════════════════════════════════════╝
                                                By Daniel Fernandez
        
          """
        print (logo)
        menu_text = """
    =================================================================================
                                    Main Menu
    =================================================================================
        1- Overall Resume.
        2- Resume by Pokemon's Type.
        3- Stats resume by Pokemon.
        4- Average level by type.
        5- Input a new pokemon.
        6- Exit.
    ---------------------------------------------------------------------------------
        """
        print(menu_text)
        main_menu_option= int(input(f"Please enter a number option:"))
   
        if main_menu_option == 1:
            print("-------------------Overall Resume------------------------")
            read_json_file(terminal_route)
            next_option=input("Please press <ENTER> to continue: <ENTER>")
            if next_option == "":
                continue
            
        elif main_menu_option == 5:
            new_pokemon_info = input_new_data()
            append_on_json_file (terminal_route, new_pokemon_info)
            next_option=input("Please press <ENTER> to continue: <ENTER>")
            if next_option == "":
                continue

        elif main_menu_option == 2:
            """
            Instrucciones 2:
                    1- Lea el archivo JSON de Pokémon
                    2- Pida al usuario un tipo de Pokémon
                    3 -Muestre todos los Pokémon que sean de ese tipo
            """  
            report_by_type(terminal_route)
            next_option=input("Please press <ENTER> to continue: <ENTER>")
            if next_option == "":
                continue
        elif main_menu_option == 3:
            """
            Instrucciones 3:
                    
                1-Lea el archivo JSON de Pokémon
                2-Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)
            """             
            report_by_stats(terminal_route)
            next_option=input("Please press <ENTER> to continue: <ENTER>")
            if next_option == "":
                continue
        elif main_menu_option == 4:
            report_by_avg_level(terminal_route)
            next_option=input("Please press <ENTER> to continue: <ENTER>")
            if next_option == "":
                continue
        elif main_menu_option == 6:
            goofbye_art = """
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║      Thanks for using Pokemon Wallet! See you!       ║
    ║                                                      ║
    ║        _.---._                                       ║
    ║      .'       '.      _                              ║
    ║     /    _     \\    (_)_      Gotta catch 'em all!   ║
    ║    |    (_)     |   (_)_                             ║
    ║     \\          /     (_)_                            ║
    ║      '._____.'                                       ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
            
            
            """
            print(goofbye_art)

            print("     Closing the program........................" \
            "" \
            "" \
            "")
            break
        else:
            print("Option Failure. Please enter a number between 1 to 6.")
    
main()