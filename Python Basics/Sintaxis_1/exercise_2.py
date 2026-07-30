#Clasificador de edades
print ("----------------Clasificador de Edades---------------")
name = input("Ingrese su nombre: ")
last_name = input("Ingrese su segundo apellido: ")
age = int(input("Ingrese su edad: "))
if age < 3:
    category = "Bebe"
    message = "¡Eres un bebé!"
elif age < 8:
    category = "Niño"
    message = "¡Eres un niño!"
elif age < 13:
    category = "Pre-adolescente"
    message = "¡Eres un pre-adolescente!"
elif age < 18:
    category = "Adolescente"
    message = "¡Eres un adolescente!"
elif age < 30:
    category = "Adulto Joven"
    message = "¡Eres un Adulto Joven!"
elif age < 60:
    category = "Adulto"
    message = "¡Eres un adulto!"    
else:
    category = "Adulto Mayor"
    message = "¡Eres un Adulto Mayor!"
print(f"{name} {last_name}, tu categoría es: {category}")
print(message)  
