import json
import os

#credential_file = "credencials.json"
credential_file = os.path.dirname(os.path.abspath(__file__))+"/credencials.json" #Estaba creando el json fuera de la carpeta destinada para el proyecto
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