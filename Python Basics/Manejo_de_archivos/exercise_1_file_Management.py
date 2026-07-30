import os
def read_song_list(root_path):
    songs = []
    try:
        with open (root_path,'r',encoding='utf-8') as file:
            lines = file.readlines()
            for number, line in enumerate(lines,start=1):
                song_name = line.strip()
                songs.append (song_name)
                print(f"Line {number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {root_path}") 
    return songs
def append_to_song_list(dest_path,write_path):
    with open(dest_path,'w',encoding='utf-8') as new_file:
        for songs in write_path:   
                new_file.write(songs + "\n")
    print(f"\nContenido pegado exitosamente en: {dest_path}")
    print("-----------------Lista Ordenada------------------")
    for number, songs in enumerate(write_path,start=1):
           print(f"Line {number}: {songs}") 


def route_file(prompt_text,base_dir):
    """Esta función permite evaluar y corregir el nombre del archivo para que siempre sea formato txt"""
    name = input(prompt_text)
    if not name.endswith(".txt"):
         name += ".txt"
    return os.path.join(base_dir,name)

def main():    
    ruta_terminal = os.path.dirname(os.path.abspath(__file__))
    root_file = route_file("Ingrese el nombre del archivo de origen:",ruta_terminal)
    destination_file = route_file("Ingrese el nombre del archivo de destino:",ruta_terminal)
    
    print(f"La ruta de orige es:{root_file}")
    print(f"La ruta de destino es:{destination_file}")

    new_list_song = read_song_list(root_file)
    new_list_song.sort(key=str.upper)
    append_to_song_list(destination_file,new_list_song)


main()