def armar_perfil (nombre:str, *habilidades, **redes):
    
    print(f"Nombre: {nombre}")
    print("Habilidades:")
    for i, skills in enumerate(habilidades, start=1):
        print(f"{i}...{skills}") 
    print("Redes:")
    for f, (networks, usser) in enumerate (redes.items(),start =1):
        print(f"{f}...{networks}:{usser}")


armar_perfil("Daniel","Inteligente", "amable", "Respetuoso", "Alegre", Facebook="Daniel_Fernandez", Instagram="Daniel_506", Linkedin="Inge_Daniel")