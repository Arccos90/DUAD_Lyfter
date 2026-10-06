"---------------------Exercise 1_ Four Pillar OOP------------------------------"

class BankAccount:
    def __init__(self, titular:str, balance: float):
        self.titular = titular
        self._balance = balance #este dato será un valor privado, no quiero que se modifique

    def get_balance(self) -> float:
        """Permite consultar el saldo de forma controlada."""
        return self._balance

    def deposit_money (self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f"Se ha realizado el deposito correctamente. Saldo Actual: ${self._balance}")
        else:
            print("El monto debe ser positivo")

    def withdraw_money (self, amount:float):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Se ha realizado el retiro correctamente. Saldo Actual: ${self._balance}")
        else:
            print("No tiene fondos suficientes en su cuenta")

class SavingAccount (BankAccount):
    def __init__ (self, titular:str, balance: float, min_balance:float):
        super().__init__(titular, balance)
        self.min_balance = min_balance
        
    def saving_money (self, amount:float):
        self.deposit_money(amount)

    def retire_money (self, amount:float):
        if amount < 0:
            raise ValueError ("El monto debe ser mayor a cero")
        elif self._balance - amount < self.min_balance:
            raise ValueError ("Operación rechazada, el saldo no puede quedar por debajo del mínimo")
        elif self._balance - amount >= self.min_balance:
            self._balance -= amount
            print(f"Retiro exitoso, su saldo actual es: ${self._balance}")
        

name = str(input("Ingrese el nombre del cliente:  ")).strip()
initial_balance = float(input("Ingrese el saldo inicial de la cuenta: $"))
min_balance = float(input("Ingrese el monto minimo de ahorro en su cuenta:  $"))
new_account = SavingAccount(name,initial_balance,min_balance)
while True:
    action = int(input("¿Que acción desea realizar? 1-Depositar / 2-Retirar:  "))
    amount = float(input("Ingrese el monto:  $"))
    try:
        if action == 1:
            new_account.deposit_money(amount)
            continue
        elif action == 2:
            new_account.retire_money(amount)
            continue
        else:
            print("Opción no válida")
            continue
    except ValueError as error:
        print(f"[Error en la transacción]: {error}")
