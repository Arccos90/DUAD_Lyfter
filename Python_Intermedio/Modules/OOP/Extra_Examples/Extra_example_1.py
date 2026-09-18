class Billetera:
    def __init__(self, titular:str, saldo_inicial:float = 0):
        self.titular = titular  
        self.monto = saldo_inicial
    def ingresar (self, nuevo_monto):
        self.monto += nuevo_monto 
        print (f"{self.titular}, su saldo es: {self.monto}")
    def gastar (self, nuevo_monto):
        if self.monto - nuevo_monto >= 0:
            self.monto -= nuevo_monto
            print (f"{self.titular}, su saldo es: {self.monto}")
            return True
        else:
            print("No tiene suficiente fondos")
            return False
        
usser_name = input("Ingrese el nombre del usuario:")
usuario_1 = Billetera (usser_name)
while True:
    mount =  float(input("Ingrese un monto:"))
    action = input("¿ que acción desea hacer? <ingresar>, <gastar> o <terminar> para salir").lower()
    if action == "ingresar":
        usuario_1.ingresar(mount)
        continue
    elif action == "gastar":
        usuario_1.gastar(mount)
        continue
    elif action == "terminar":
        print("Gracias por usar el sistema, bye!!")
        break


