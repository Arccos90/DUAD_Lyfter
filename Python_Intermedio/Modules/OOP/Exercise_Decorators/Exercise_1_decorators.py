"---------------------Exercise_1: Decoradores"
def function_notification (func):

    def wrapper (*args, **kwargs):
        print(f"ejecutando: {func.__name__}")
        print (f"Argumentos posicionales (*args): {args}")
        print (f"Keyword arguments (**kwargs): {kwargs}")
        resultado = func(*args,**kwargs)
        print(f"Retorno de la funcion {resultado}")
        print("¡funcion ejecutada con éxito!")
        return resultado
    return wrapper
    
@ function_notification
def create_profile (nombre:str,*habilidades:str, **redes:str ):
        print(f"Nombre: {nombre}")
        print("Habilidades:")
        for i, skills in enumerate(habilidades, start=1):
            print(f"{i}...{skills}") 
        print("Redes:")
        for f, (networks, usser) in enumerate (redes.items(),start =1):
            print(f"{f}...{networks}:{usser}")

        return f"perfil de {nombre} creado correctamente"

create_profile("Daniel","Inteligente", "amable", "Respetuoso", "Alegre", Facebook="Daniel_Fernandez", Instagram="Daniel_506", Linkedin="Inge_Daniel")