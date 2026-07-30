#Ejercicios de SIntaxis
print("Daniel" + "Fernàndez")
print("Daniel" + 1989) #Esto dará un error porque no se pueden concatenar una cadena con un número
print (55 + "Fernandez") #Esto también dará un error por la misma razón
print (["Manzana", "Banana"] + ["Naranja", "Pera"]) #Esto concatenará las dos listas
print ("Daniel" + ["Fernandez","Ramirez"]) #Esto dará un error porque no se pueden concatenar una cadena con una lista
print (55+[15,45,55,65]) #Esto dará un error porque no se pueden concatenar un número con una lista
print (float(55.34+25.45)) #Esto sumará los dos números y luego convertirá el resultado a un número de punto flotante
print (float(55.34)+55) #Esto convertirá el número 55.34 a un número de punto flotante (aunque ya lo es) y luego sumará 55, dando como resultado 110.34
print (True + True) #Esto sumará los dos valores booleanos y dara como resultado 2
print (True + False) #Esto sumará los dos valores booleanos y dara como resultado 1
print (False + False) #Esto sumará los dos valores booleanos y dara como resultado 0
