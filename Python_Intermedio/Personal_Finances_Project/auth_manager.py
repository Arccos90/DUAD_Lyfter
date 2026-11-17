import json
import os

#credential_file = "credentials.json"
credential_file = os.path.dirname(os.path.abspath(__file__))+"/credentials.json" #Estaba creando el json fuera de la carpeta destinada para el proyecto

def process_new_user(username: str, password: str):
    clean_username = username.strip()
    clean_password = password.strip()
    if not clean_username:
        raise ValueError("El nombre de usuario no puede estar vacío.")
    
    if not clean_password:
        raise ValueError("La contraseña no puede estar vacía.")

    # Si pasa las validaciones, procedes a guardar las credenciales
    # ...


def load_credentials():
    if not os.path.exists(credential_file):
        return None
    with open(credential_file, 'r') as file:
        return json.load(file)

def save_credentials(username, password, security_answer):
    data = {
        "username": username,
        "password": password,
        "security_answer": security_answer
    }
    with open(credential_file, 'w') as file:
        json.dump(data, file)