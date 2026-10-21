print("------------------------Excercise_3: Decorators------------------------")

from datetime import date
class User :
    def __init__(self,name:str, date_of_birth):
        self.date_of_birth = date_of_birth
        self.name = name

    @property
    def age (self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day): # si no ha cumplido anos aun deja la edad actual.
            age -= 1
        print(f"{self.name} tiene {age} años!")
        return age
    
def age_validator(func):
    def wrapper(*args, **kwargs):
        print(f"ejecutando: {func.__name__}")
        #print (f"Argumentos posicionales (*args): {args}")
        #print (f"Keyword arguments (**kwargs): {kwargs}")
        user_instance = args [0]
        #print (f"{user_instance.age}")
        if user_instance.age < 18:
            raise ValueError (f"No puede ingresar, {user_instance.name}, nació {user_instance.date_of_birth}, no es mayor de edad!")
        result = func(*args,**kwargs)
        print (f"fin de ejecucion {func.__name__}")
        return result
    return wrapper

    
@age_validator
def access_control (user: User,invitation: bool):
    if invitation == False:
        print("Lo siento, No puede ingresar")
    else:
        print(f"Bienvenido {user.name}, puede ingresar, tiene invitación!")



name = str(input("Ingrese el nombre: "))
print("Ingrese la fecha de nacimiento:")
year = int(input("Año: "))
month = int(input("Número de Mes: "))
day = int(input("Número de día: "))

inv_input = (input("Tiene invitación? (True/False): ")).strip().capitalize()
invitation = True if inv_input == "True" else False

date_of_birth = date(year, month, day)
new_user = User(name, date_of_birth)
try:
    access_control (new_user,invitation)
except ValueError as error:
    print (f"error capturado:  {error}")



